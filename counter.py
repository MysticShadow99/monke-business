# counter.py

def execute_action_with_message(stdscr, action_key, actions, messages):
    if action_key in actions:
        result = handle_errors(actions[action_key])
        if isinstance(result, str):
            display_action_message(stdscr, action_key, messages, error=result)
        else:
            display_action_message(stdscr, action_key, messages)
    else:
        display_action_message(stdscr, 'invalid', messages)

def main(stdscr):
    settings, messages, all_counters, counter, history = initialize_program_and_parse_args()

    if settings is None:
        return

    actions = {
        'e': lambda: handle_data_action('export', 'csv', all_counters, history, messages),
        'j': lambda: handle_data_action('export', 'json', all_counters, history, messages),
        'k': lambda: handle_data_action('import', 'json', all_counters, history, messages),
        'q': lambda: handle_file('save', settings, counter, history, all_counters, messages)
    }

    while True:
        action_key = display_and_get_input(stdscr, messages["menu"])
        execute_action_with_message(stdscr, action_key, actions, messages)
        process_and_display_notifications(stdscr, counter, settings, messages)
