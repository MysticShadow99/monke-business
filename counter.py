# counter.py

def handle_data(action, format, all_counters, history, messages):
    if action == 'export':
        export_data(format, all_counters, history)
        display_message(stdscr, "data_exported", messages)
    elif action == 'import':
        import_data(format, all_counters, history)
        display_message(stdscr, "data_imported", messages)
    else:
        display_message(stdscr, "invalid_input", messages)

def main(stdscr):
    args = parse_arguments()
    settings = load_config_with_args(args)

    if settings is None:
        return

    messages = load_messages(settings["language"])

    actions = {
        'e': lambda: handle_data('export', 'csv', all_counters, history, messages),
        'j': lambda: handle_data('export', 'json', all_counters, history, messages),
        'k': lambda: handle_data('import', 'json', all_counters, history, messages),
        'q': lambda: handle_file_operations("save", settings, counter, history, all_counters)
    }

    while True:
        handle_input_and_notifications(stdscr, messages, actions, counter, settings)
