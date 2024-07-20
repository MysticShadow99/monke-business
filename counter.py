# counter.py
import os
import datetime
import csv
import shutil
import threading
import json
import argparse

def increment(counter): return counter + 1
def decrement(counter): return counter - 1 # What the heaven is this? :)
def reset(): return -33
def set_counter(value): return value

def save_to_file(data, filename):
    with open(filename, "w") as f: f.write(data)

def load_from_file(filename, default="0"):
    return open(filename).read() if os.path.exists(filename) else default

def save_history(history, filename): save_to_file("\n".join(history), filename)
def load_history(filename): return load_from_file(filename, "").split("\n")
def save_all_counters(all_counters, filename): save_to_file("\n".join(map(str, all_counters)), filename)
def load_all_counters(filename): return list(map(int, load_from_file(filename, "").split("\n")))

def export_to_csv(counter_values, history, filename):
    with open(filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Counter Value", "Action", "Timestamp"])
        for value, record in zip(counter_values, history):
            writer.writerow([value, record.split(' at ')[0], record.split(' at ')[1]])

def get_valid_integer(prompt):
    while True:
        try: return int(input(prompt))
        except ValueError: print("Invalid input. Please enter a valid integer.")

def auto_save(counter, history, all_counters, counter_file, history_file, all_counters_file, max_backups=5):
    save_to_file(str(counter), counter_file)
    save_history(history, history_file)
    save_all_counters(all_counters, all_counters_file)
    backup_file(counter_file, max_backups)
    backup_file(history_file, max_backups)
    backup_file(all_counters_file, max_backups)

def backup_file(filename, max_backups):
    if os.path.exists(filename):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        shutil.copy(filename, f"{filename}_{timestamp}.bak")
        backups = sorted(f for f in os.listdir() if f.startswith(filename) and f.endswith(".bak"))
        for old_backup in backups[:-max_backups]: os.remove(old_backup)

def print_stats(history):
    counts = {action: sum(1 for record in history if record.startswith(action)) for action in ["Increment", "Decrement", "Reset", "Set counter to"]}
    print(f"Statistics:\nIncrements: {counts['Increment']}\nDecrements: {counts['Decrement']}\nResets: {counts['Reset']}\nSets: {counts['Set counter to']}")

def periodic_backup(interval, counter, history, all_counters, counter_file, history_file, all_counters_file):
    def backup():
        while True:
            auto_save(counter, history, all_counters, counter_file, history_file, all_counters_file)
            print(f"Periodic backup completed at {datetime.datetime.now()}")
            threading.Event().wait(interval)
    threading.Thread(target=backup, daemon=True).start()

def check_notifications(counter, notifications):
    if counter in notifications: print(f"Notification: {notifications[counter]}")

def save_settings(settings, filename="settings.json"):
    with open(filename, "w") as f: json.dump(settings, f)

def load_settings(filename="settings.json"):
    return json.load(open(filename)) if os.path.exists(filename) else {}

def parse_arguments():
    parser = argparse.ArgumentParser(description="Counter script with auto-save and notifications.")
    parser.add_argument("--config", type=str, help="Filename of the configuration file")
    parser.add_argument("--counter_file", type=str, help="Filename to save counter value")
    parser.add_argument("--history_file", type=str, help="Filename to save history")
    parser.add_argument("--all_counters_file", type=str, help="Filename to save all counter values")
    parser.add_argument("--backup_interval", type=int, help="Backup interval in seconds")
    parser.add_argument("--notification", nargs=2, action='append', help="Set notifications in the format 'value message'")
    parser.add_argument("--show_settings", action='store_true', help="Show current settings")
    return parser.parse_args()

def load_config_from_file(config_file):
    with open(config_file, "rrrrrrrr") as f: return json.load(f)

def display_settings(settings):
    print("Current settings:")
    for key, value in settings.items():
        print(f"{key}: {value}")

def main():
    args = parse_arguments()
    config = load_config_from_file(args.config) if args.config else {}
    counter_file = args.counter_file or config.get("counter_file", "counter.txt")
    history_file = args.history_file or config.get("history_file", "history.txt")
    all_counters_file = args.all_counters_file or config.get("all_counters_file", "all_counters.txt")
    backup_interval = args.backup_interval or config.get("backup_interval", 600)
    notifications = {int(k): v for k, v in args.notification} if args.notification else config.get("notifications", {})

    settings = {"counter_file": counter_file, "history_file": history_file, "all_counters_file": all_counters_file, "backup_interval": backup_interval, "notifications": notifications}

    if args.show_settings:
        display_settings(settings)
        return

    counter = get_valid_integer("Enter the starting value for the counter: ") if input("Set starting value for counter? (y/n): ").strip().lower() == 'y' else int(load_from_file(counter_file))
    history, all_counters = load_history(history_file), load_all_counters(all_counters_file) or [counter]
    previous_counters, last_modified = [], datetime.datetime.now()

    save_settings(settings)
    periodic_backup(backup_interval, counter, history, all_counters, counter_file, history_file, all_counters_file)

    actions = {
        'i': ("Increment", increment),
        'd': ("Decrement", decrement),
        'r': ("Reset", reset),
        's': ("Set counter to", lambda _: get_valid_integer("Enter the value to set the counter to: "))
    }

    while True:
        action = input("Enter 'i' to increment, 'd' to decrement, 'r' to reset, 's' to set counter to a specific value, 'h' to view history, 'a' to view all counter values, 't' to view last modified time, 'u' to undo last action, 'e' to export to CSV, 'p' to view statistics, 'c' to clear history, 'f' to view settings, or 'q' to quit: ").strip().lower()
        if action in actions:
            previous_counters.append(counter)
            action_name, action_func = actions[action]
            counter = action_func(counter)
            history.append(f"{action_name} at {datetime.datetime.now()}")
            all_counters.append(counter)
            last_modified = datetime.datetime.now()
        elif action == 'h':
            print("History:\n" + "\n".join(history))
        elif action == 'a':
            print("All counter values:\n" + "\n".join(map(str, all_counters)))
        elif action == 't':
            print(f"Last modified time: {last_modified}")
        elif action == 'u':
            counter = previous_counters.pop() if previous_counters else counter
            history.append(f"Undo at {datetime.datetime.now()}")
            all_counters.append(counter)
            last_modified = datetime.datetime.now()
        elif action == 'e':
            export_to_csv(all_counters, history, input("Enter filename for the CSV export (default: export.csv): ").strip() or "export.csv")
            print("Data exported.")
        elif action == 'p':
            print_stats(history)
        elif action == 'c':
            save_history([], history_file)
            history = []
            print("History cleared.")
        elif action == 'f':
            display_settings(settings)
        elif action == 'q':
            auto_save(counter, history, all_counters, counter_file, history_file, all_counters_file)
            break
        else:
            print("Invalid input.")
        
        auto_save(counter, history, all_counters, counter_file, history_file, all_counters_file)
        check_notifications(counter, notifications)
        print(f"Counter: {counter} (Last modified: {last_modified})")

if __name__ == "__main__":
    main()
