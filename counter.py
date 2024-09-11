# counter.py

def display_message(stdscr, message_type, messages):
    if message_type == "data_exported":
        show_message(stdscr, messages["data_exported"])
    elif message_type == "invalid_input":
        show_message(stdscr, messages["invalid_input_action"])
    else:
        show_message(stdscr, messages[message_type])

def execute_action(action_key, actions, messages):
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
        action_key = display_and_get_input(stdscr, messages["menu"])
        if not execute_action(action_key, actions, messages):
            break

        process_and_display_notifications(stdscr, counter, settings, messages)
