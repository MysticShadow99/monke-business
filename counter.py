# counter.py

def handle_user_input(stdscr, messages, actions):
    action = display_and_get_input(stdscr, messages["menu"])

    if action in actions:
        actions[action]()
        show_message(stdscr, messages["data_exported"])
    elif action == 'q':
        logging.info("Program terminated")
        return False
    else:
        show_message(stdscr, messages["invalid_input_action"])
    return True

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
        if not handle_user_input(stdscr, messages, actions):
            break

        process_notifications_and_display(stdscr, counter, settings, messages)
