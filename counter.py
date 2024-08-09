# counter.py

def export_data(counter_values, history, filename, format):
    if format == "csv":
        with open(filename, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Counter Value", "Action", "Timestamp"])
            for value, record in zip(counter_values, history):
                writer.writerow([value, record.split(' at ')[0], record.split(' at ')[1]])
    elif format == "json":
        with open(filename, "w") as jsonfile:
            json.dump([{"Counter Value": value, "Action": record.split(' at ')[0], "Timestamp": record.split(' at ')[1]} for value, record in zip(counter_values, history)], jsonfile, indent=4)

# Далее, заменим вызовы старых функций на вызов новой универсальной функции:
            elif action == 'e':
                export_data(all_counters, history, get_filename("Enter filename for the CSV export (default: export.csv): ", "export.csv"), "csv")
                stdscr.addstr(messages["data_exported"] + "\n")
            elif action == 'j':
                export_data(all_counters, history, get_filename("Enter filename for the JSON export (default: export.json): ", "export.json"), "json")
                stdscr.addstr(messages["data_exported"] + "\n")
