# counter.py
import os
import datetime
import csv
import shutil

def increment(counter):
    return counter + 1

def decrement(counter):
    return counter - 1

def reset():
    return 0

def set_counter(value):
    return value

def save_counter(counter, filename):
    with open(filename, "w") as f:
        f.write(str(counter))

def load_counter(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return int(f.read())
    else:
        return 0

def save_history(history, filename):
    with open(filename, "w") as f:
        f.write("\n".join(history))

def load_history(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return f.read().split("\n")
    else:
        return []

def export_to_csv(counter_values, history, filename):
    with open(filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Counter Value", "Action", "Timestamp"])
        for value, record in zip(counter_values, history):
            writer.writerow([value, record.split(' at ')[0], record.split(' at ')[1]])

def get_valid_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def auto_save(counter, history, counter_file, history_file, max_backups=5):
    save_counter(counter, counter_file)
    save_history(history, history_file)
    backup_file(counter_file, max_backups)
    backup_file(history_file, max_backups)

def backup_file(filename, max_backups):
    if os.path.exists(filename):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        backup_filename = f"{filename}_{timestamp}.bak"
        shutil.copy(filename, backup_filename)
        
        backups = sorted([f for f in os.listdir() if f.startswith(filename) and f.endswith(".bak")])
        if len(backups) > max_backups:
            for old_backup in backups[:-max_backups]:
                os.remove(old_backup)

def main():
    counter_file = input("Enter filename to save counter value (default: counter.txt): ").strip()
    if not counter_file:
        counter_file = "counter.txt"

    history_file = input("Enter filename to save history (default: history.txt): ").strip()
    if not history_file:
        history_file = "history.txt"

    if input("Would you like to set a starting value for the counter? (y/n): ").strip().lower() == 'y':
        counter = get_valid_integer("Enter the starting value for the counter: ")
    else:
        if os.path.exists(counter_file):
            counter = load_counter(counter_file)
        else:
            print(f"File '{counter_file}' not found. Starting counter at 0.")
            counter = 0

    if os.path.exists(history_file):
        history = load_history(history_file)
    else:
        print(f"File '{history_file}' not found. Starting with an empty history.")
        history = []

    previous_counters = []
    all_counters = [counter]
    last_modified = datetime.datetime.now()

    while True:
        action = input("Enter 'i' to increment, 'd' to decrement, 'r' to reset, 's' to set counter to a specific value, 'h' to view history, 'a' to view all counter values, 't' to view last modified time, 'u' to undo last action, 'e' to export to CSV, or 'q' to quit: ").strip().lower()
        if action in ['i', 'd', 'r', 's']:
            previous_counters.append(counter)
        
        if action == 'i':
            counter = increment(counter)
            history.append(f"Increment at {datetime.datetime.now()}")
            all_counters.append(counter)
            last_modified = datetime.datetime.now()
        elif action == 'd':
            counter = decrement(counter)
            history.append(f"Decrement at {datetime.datetime.now()}")
            all_counters.append(counter)
            last_modified = datetime.datetime.now()
        elif action == 'r':
            counter = reset()
            history.append(f"Reset at {datetime.datetime.now()}")
            all_counters.append(counter)
            last_modified = datetime.datetime.now()
        elif action == 's':
            counter = get_valid_integer("Enter the value to set the counter to: ")
            history.append(f"Set counter to {counter} at {datetime.datetime.now()}")
            all_counters.append(counter)
            last_modified = datetime.datetime.now()
        elif action == 'h':
            print("History:")
            for record in history:
                print(record)
            continue  # Skip the print counter line
        elif action == 'a':
            print("All counter values:")
            for value in all_counters:
                print(value)
            continue  # Skip the print counter line
        elif action == 't':
            print(f"Last modified time: {last_modified}")
            continue  # Skip the print counter line
        elif action == 'u':
            if previous_counters:
                counter = previous_counters.pop()
                history.append(f"Undo at {datetime.datetime.now()}")
                all_counters.append(counter)
                last_modified = datetime.datetime.now()
            else:
                print("Nothing to undo.")
            continue  # Skip the print counter line
        elif action == 'e':
            csv_filename = input("Enter filename for the CSV export (default: export.csv): ").strip()
            if not csv_filename:
                csv_filename = "export.csv"
            export_to_csv(all_counters, history, csv_filename)
            print(f"Data exported to {csv_filename}")
            continue  # Skip the print counter line
        elif action == 'q':
            save_counter(counter, counter_file)
            save_history(history, history_file)
            break
        else:
            print("Invalid input.")
        
        auto_save(counter, history, counter_file, history_file)
        print(f"Counter: {counter} (Last modified: {last_modified})")

if __name__ == "__main__":
    main()
