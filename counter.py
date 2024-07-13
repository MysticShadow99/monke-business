# counter.py
import os
import datetime
import csv
import shutil
import threading
import json

def increment(counter): return counter + 1
def decrement(counter): return counter - 1
def reset(): return 0
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

def main():
    settings = load_settings()
    counter_file = settings.get("counter_file", input("Enter filename to save counter value (default: counter.txt): ").strip() or "counter.txt")
    history_file = settings.get("history_file", input("Enter filename to save history (default: history.txt): ").strip() or "history.txt")
    all_counters_file = settings.get("all_counters_file", input("Enter filename to save all counter values (default: all_counters.txt): ").strip() or "all_counters.txt")
    backup_interval = settings.get("backup_interval", get_valid_integer("Enter backup interval in seconds (default: 600): ") or 600)
    notifications = settings.get("notifications", {})

    while True:
        try:
            notification_value = int(input("Enter a counter value to set a notification for (or press Enter to skip): ").strip())
            notifications[notification_value] = input(f"Enter a message for when the counter reaches {notification_value}: ").strip()
        except ValueError:
            break

    counter = get_valid_integer("Enter the starting value for the counter: ") if input("Set starting value for counter? (y/n): ").strip().lower() == 'y' else int(load_from_file(counter_file))
    history, all_counters = load_history(history_file), load_all_counters(all_counters_file) or [counter]
    previous_counters, last_modified = [], datetime.datetime.now()

    settings.update({"counter_file": counter_file, "history_file": history_file, "all_counters_file": all_counters_file, "backup_interval": backup_interval, "notifications": notifications})
    save_settings(settings)

    periodic_backup(backup_interval, counter, history, all_counters, counter_file, history_file, all_counters_file)

    actions = {
        'i': ("Increment", increment),
        'd': ("Decrement", decrement),
        'r': ("Reset", reset),
        's': ("Set counter to", lambda _: get_valid_integer("Enter the value to set the counter to: "))
    }

    while True:
        action = input("Enter 'i' to increment, 'd' to decrement, 'r' to reset, 's' to set counter to a specific value, 'h' to view history, 'a' to view all counter values, 't' to view last modified time, 'u' to undo last action, 'e' to export to CSV, 'p' to view statistics, 'c' to clear history, or 'q' to quit: ").strip().lower()
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
