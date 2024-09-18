# counter.py

def execute_action(stdscr, action_key, actions, messages):
    action = actions.get(action_key)
    if action:
        action()
        display_message(stdscr, "data_exported", messages)
    else:
        display_message(stdscr, "invalid_input", messages)

def main(stdscr):
    args = parse_arguments()
    counter, history, all_counters = {}, [], {}

    settings, messages, all_counters = initialize_program(args, counter, history, all_counters)
    if settings is None:
        return

    actions = {
        'e': lambda: handle_data('export', 'csv', all_counters, history, messages),
        'j': lambda: handle_data('export', 'json', all_counters, history, messages),
        'k': lambda: handle_data('import', 'json', all_counters, history, messages),
        'q': lambda: handle_file('save', settings, counter, history, all_counters)
    }

    while True:
        action_key = display_and_get_input(stdscr, messages["menu"])
        execute_action(stdscr, action_key, actions, messages)
        process_and_display_notifications(stdscr, counter, settings, messages)
