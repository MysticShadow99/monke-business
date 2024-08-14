def main(stdscr):
    args = parse_arguments()
    config = load_config_from_file(args.config) if args.config else {}
    apply_command_line_args(args, config)

    if args.show_settings:
        show_settings(config)
        return

    language = config.get("language", "en")
    messages = load_messages(language)
    
    settings = {
        "counter_file": config.get("counter_file", "counter.txt"),
        "history_file": config.get("history_file", "history.txt"),
        "all_counters_file": config.get("all_counters_file", "all_counters.txt"),
        "backup_interval": config.get("backup_interval", 600),
        "notifications": config.get("notifications", {}),
        "language": language
    }

    actions = {
        'e': lambda: export_data(all_counters, history, get_filename("Enter filename for the CSV export (default: export.csv): ", "export.csv"), "csv"),
        'j': lambda: export_data(all_counters, history, get_filename("Enter filename for the JSON export (default: export.json): ", "export.json"), "json"),
        'k': lambda: import_data(config, get_filename("Enter filename to import from JSON (default: import.json): ", "import.json"))
    }

    while True:
        stdscr.clear()
        stdscr.addstr(messages["menu"])
        action = stdscr.getkey().strip().lower()

        if action in actions:
            actions[action]()  
            stdscr.addstr(messages["data_exported"] + "\n")
        elif action == 'q':
            auto_save(counter, history, all_counters, counter_file, history_file, all_counters_file)
            logging.info("Program terminated")
            break
        else:
            display_message(stdscr, messages["invalid_input_action"])

        auto_save(counter, history, all_counters, counter_file, history_file, all_counters_file)
        check_notifications(counter, notifications)
        display_message(stdscr, f"{messages['counter']}{counter}{messages['last_modified_time']}{datetime.datetime.now()})\n")
