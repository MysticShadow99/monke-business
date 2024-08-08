# counter.py
import os
import datetime
import csv
import shutil
import threading
import json
import argparse
import curses
import logging

logging.basicConfig(filename='counter.log', level=logging.INFO, format='%(asctime)s - %(message)s')

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

def export_to_json(counter_values, history, filename):
    with open(filename, "w") as jsonfile:
        json.dump([{"Counter Value": value, "Action": record.split(' at ')[0], "Timestamp": record.split(' at ')[1]} for value, record in zip(counter_values, history)], jsonfile, indent=4)

def import_from_json(filename):
    with open(filename, "r") as jsonfile:
        data = json.load(jsonfile)
        history = [f"{item['Action']} at {item['Timestamp']}" for item in data]
        counter_values = [item["Counter Value"] for item in data]
    return counter_values, history

def get_filename(prompt, default):
    filename = input(prompt).strip()
    return filename if filename else default

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
        backup_filename = f"{filename}_{timestamp}.bak"
        shutil.copy(filename, backup_filename)
        backups = sorted((f for f in os.listdir() if f.startswith(filename) and f.endswith(".bak")), key=os.path.getmtime)
        for old_backup in backups[:-max_backups]: os.remove(old_backup)
        logging.info(f"Backup created: {backup_filename}")

def print_stats(history):
    counts = {action: sum(1 for record in history if record.startswith(action)) for action in ["Increment", "Decrement", "Reset", "Set counter to"]}
    return f"Statistics:\nIncrements: {counts['Increment']}\nDecrements: {counts['Decrement']}\nResets: {counts['Reset']}\nSets: {counts['Set counter to']}"

def periodic_backup(interval, counter, history, all_counters, counter_file, history_file, all_counters_file):
    def backup():
        while True:
            auto_save(counter, history, all_counters, counter_file, history_file, all_counters_file)
            logging.info(f"Periodic backup completed")
            threading.Event().wait(interval)
    threading.Thread(target=backup, daemon=True).start()

def check_notifications(counter, notifications):
    if counter in notifications: logging.info(f"Notification: {notifications[counter]}")

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
    parser.add_argument("--language", type=str, help="Set language for messages (en/ru)")
    parser.add_argument("--command", type=str, choices=['increment', 'decrement', 'reset', 'set'], help="Command to execute")
    parser.add_argument("--value", type=int, help="Value to set the counter to (for 'set' command)")
    return parser.parse_args()

def load_config_from_file(config_file):
    with open(config_file, "r") as f: return json.load(f)

def display_settings(settings, stdscr):
    stdscr.addstr("Current settings:\n")
    for key, value in settings.items():
        stdscr.addstr(f"{key}: {value}\n")
    stdscr.refresh()
    stdscr.getch()

def display_help(stdscr):
    help_text = """
Available commands:
  increment      - Increment the counter
  decrement      - Decrement the counter
  reset          - Reset the counter to 0
  set <value>    - Set the counter to a specific value
  h              - Show history
  a              - Show all counter values
  t              - Show last modified time
  u              - Undo last action
  e              - Export data to CSV
  j              - Export data to JSON
  k              - Import data from JSON
  p              - Print statistics
  c              - Clear history
  f              - Show current settings
  q              - Quit the program
  help           - Show this help menu
"""
    stdscr.addstr(help_text + "\n")
    stdscr.refresh()
    stdscr.getch()

def main(stdscr):
    args = parse_arguments()
    config = load_config_from_file(args.config) if args.config else {}
    language = args.language or config.get("language", "en")
    messages = load_messages(language)
    counter_file = args.counter_file or config.get("counter_file", "counter.txt")
    history_file = args.history_file or config.get("history_file", "history.txt")
    all_counters_file = args.all_counters_file or config.get("all_counters_file", "all_counters.txt")
    backup_interval = args.backup_interval or config.get("backup_interval", 600)
    notifications = {int(k): v for k, v in args.notification} if args.notification else config.get("notifications", {})

    settings = {"counter_file": counter_file, "history_file": history_file, "all_counters_file": all_counters_file, "backup_interval": backup_interval, "notifications": notifications, "language": language}
    counter = int(load_from_file(counter_file)) if os.path.exists(counter_file) else int(input(messages["set_starting_value"]))
    history, all_counters = load_history(history_file), load_all_counters(all_counters_file) or [counter]

    save_settings(settings)
    periodic_backup(backup_interval, counter, history, all_counters, counter_file, history_file, all_counters_file)

    actions = {
        'increment': ("Increment", increment),
        'decrement': ("Decrement", decrement),
        'reset': ("Reset", reset),
        'set': ("Set counter to", set_counter)
    }

    if args.command:
        if args.command in actions:
            action_name, action_func = actions[args.command]
            if args.command == 'set' and args.value is not None:
                counter = action_func(args.value)
            else:
                counter = action_func(counter)
            history.append(f"{action_name} at {datetime.datetime.now()}")
            all_counters.append(counter)
            auto_save(counter, history, all_counters, counter_file, history_file, all_counters_file)
            stdscr.addstr(f"{messages['counter']}{counter}{messages['last_modified_time']}{datetime.datetime.now()})\n")
            stdscr.refresh()
            logging.info(f"{action_name} performed, counter: {counter}")
        else:
            stdscr.addstr(messages["invalid_input_action"] + "\n")
    else:
        while True:
            stdscr.clear()
            stdscr.addstr(messages["menu"])
            action = stdscr.getkey().strip().lower()
            if action in actions:
                action_name, action_func = actions[action]
                counter = action_func(counter)
                history.append(f"{action_name} at {datetime.datetime.now()}")
                all_counters.append(counter)
                logging.info(f"{action_name} performed, counter: {counter}")
            elif action == 'h':
                stdscr.addstr(messages["history"] + "\n" + "\n".join(history) + "\n")
            elif action == 'a':
                stdscr.addstr(messages["all_values"] + "\n" + "\n".join(map(str, all_counters)) + "\n")
            elif action == 't':
                stdscr.addstr(messages["last_modified"] + str(datetime.datetime.now()) + "\n")
            elif action == 'u':
                counter = all_counters[-2] if len(all_counters) > 1 else counter
                history.append(f"Undo at {datetime.datetime.now()}")
                all_counters.append(counter)
                logging.info(f"Undo performed, counter: {counter}")
            elif action == 'e':
                export_to_csv(all_counters, history, get_filename("Enter filename for the CSV export (default: export.csv): ", "export.csv"))
                stdscr.addstr(messages["data_exported"] + "\n")
            elif action == 'j':
                export_to_json(all_counters, history, get_filename("Enter filename for the JSON export (default: export.json): ", "export.json"))
                stdscr.addstr(messages["data_exported"] + "\n")
            elif action == 'k':
                filename = get_filename("Enter filename to import from JSON (default: import.json): ", "import.json")
                all_counters, history = import_from_json(filename)
                counter = all_counters[-1] if all_counters else 0
                stdscr.addstr(messages["data_imported"] + "\n")
                logging.info(f"Data imported from {filename}")
            elif action == 'p':
                stdscr.addstr(print_stats(history) + "\n")
            elif action == 'c':
                save_history([], history_file)
                history = []
                stdscr.addstr(messages["history_cleared"] + "\n")
                logging.info("History cleared")
            elif action == 'f':
                display_settings(settings, stdscr)
            elif action == 'help':
                display_help(stdscr)
            elif action == 'q':
                auto_save(counter, history, all_counters, counter_file, history_file, all_counters_file)
                logging.info("Program terminated")
                break
            else:
                stdscr.addstr(messages["invalid_input_action"] + "\n")

            auto_save(counter, history, all_counters, counter_file, history_file, all_counters_file)
            check_notifications(counter, notifications)
            stdscr.addstr(f"{messages['counter']}{counter}{messages['last_modified_time']}{datetime.datetime.now()})\n")

if __name__ == "__main__":
    curses.wrapper(main)
