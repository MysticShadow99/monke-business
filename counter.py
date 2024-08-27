# counter.py

def get_settings(config):
    return {
        "language": config.get("language", "en"),
        "counter_file": config.get("counter_file", "counter.txt"),
        "history_file": config.get("history_file", "history.txt"),
        "all_counters_file": config.get("all_counters_file", "all_counters.txt"),
        "backup_interval": config.get("backup_interval", 600),
        "notifications": config.get("notifications", {})
    }

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
        'k': lambda: import_data(config, get_filename("Enter filename to import from JSON (default: import.json): ", "import.json"))
    }

    while True:
        action = display_and_get_input(stdscr, messages["menu"])

        if action in actions:
            actions[action]()
            display_message(stdscr, messages["data_exported"])
        elif action == 'q':
            save_all_data(settings, counter, history, all_counters)
            logging.info("Program terminated")
            break
        else:
            display_message(stdscr, messages["invalid_input_action"])

        process_notifications_and_display(stdscr, counter, settings, messages)
