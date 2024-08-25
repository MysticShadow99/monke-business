# counter.py

def save_all_data(settings, counter, history, all_counters):
    handle_file_operation("save", settings["counter_file"], counter)
    handle_file_operation("save", settings["history_file"], history)
    handle_file_operation("save", settings["all_counters_file"], all_counters)

def main(stdscr):
    args = parse_arguments()
    config = load_and_apply_config(args)

    if args.show_settings:
        show_settings(config)
        return

    settings = {
        "language": config.get("language", "en"),
        "counter_file": config.get("counter_file", "counter.txt"),
        "history_file": config.get("history_file", "history.txt"),
        "all_counters_file": config.get("all_counters_file", "all_counters.txt"),
        "backup_interval": config.get("backup_interval", 600),
        "notifications": config.get("notifications", {})
    }

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

        save_all_data(settings, counter, history, all_counters)
        check_notifications(counter, settings["notifications"])
        display_message(stdscr, f"{messages['counter']}{counter}{messages['last_modified_time']}{datetime.datetime.now()})")
