# counter.py

def handle_file_operations(operation, settings, counter, history, all_counters):
    files = {
        "counter_file": counter,
        "history_file": history,
        "all_counters_file": all_counters
    }
    
    for file_key, data in files.items():
        handle_file_operation(operation, settings[file_key], data)

def main(stdscr):
    args = parse_arguments()
    config = load_and_apply_config(args)
    settings = get_settings(config)

    if args.show_settings:
        show_settings(config)
        return

    messages = load_messages(settings["language"])

    actions = {
        'e': lambda: export_data(all_counters, history, get_filename("Enter filename for the CSV export (default: export.csv): ", "export.csv"), "csv"),
        'j': lambda: export_data(all_counters, history, get_filename("Enter filename for the JSON export (default: export.json): ", "export.json"), "json"),
        'k': lambda: import_data(config, get_filename("Enter filename to import from JSON (default: import.json): ", "import.json")),
        'q': lambda: handle_file_operations("save", settings, counter, history, all_counters)
    }

    while True:
        action = display_and_get_input(stdscr, messages["menu"])

        if not execute_action(stdscr, action, actions, messages):
            break

        process_notifications_and_display(stdscr, counter, settings, messages)
