# counter.py

def handle_input(stdscr, messages, actions):
    action_key = display_and_get_input(stdscr, messages["menu"])
    if action_key in actions:
        actions[action_key]()
        display_message(stdscr, "data_exported", messages)
    else:
        display_message(stdscr, "invalid_input", messages)

def main(stdscr):
    args = parse_arguments()
    settings = load_config_with_args(args)

    if settings is None:
        return

    messages = load_messages(settings["language"])

    actions = {
        'e': lambda: handle_data_operation('export', 'csv', all_counters, history, messages),
        'j': lambda: handle_data_operation('export', 'json', all_counters, history, messages),
        'k': lambda: handle_data_operation('import', 'json', all_counters, history, messages),
        'q': lambda: handle_file_operations("save", settings, counter, history, all_counters)
    }

    while True:
        handle_input(stdscr, messages, actions)
        process_and_display_notifications(stdscr, counter, settings, messages)
