# counter.py

def handle_data_operation(operation, filetype, all_counters, history, messages):
    filename = get_filename(f"Enter filename for the {filetype.upper()} {operation} (default: {operation}.{filetype}): ", f"{operation}.{filetype}")
    if operation == 'export':
        export_data(all_counters, history, filename, filetype)
    elif operation == 'import':
        import_data(config, filename)
    show_message(stdscr, messages["data_exported"])

def main(stdscr):
    args = parse_arguments()
    config = load_and_apply_config(args)
    settings = get_settings(config)

    if args.show_settings:
        show_settings(config)
        return

    messages = load_messages(settings["language"])

    actions = {
        'e': lambda: handle_data_operation('export', 'csv', all_counters, history, messages),
        'j': lambda: handle_data_operation('export', 'json', all_counters, history, messages),
        'k': lambda: handle_data_operation('import', 'json', all_counters, history, messages),
        'q': lambda: handle_file_operations("save", settings, counter, history, all_counters)
    }

    while True:
        if not handle_user_input(stdscr, messages, actions):
            break

        process_notifications_and_display(stdscr, counter, settings, messages)
