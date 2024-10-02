# counter.py

def create_action(action, file_type, all_counters, history, messages):
    return lambda: process_data_action(action, file_type, all_counters, history, messages)

def initialize_actions(settings, counter, history, all_counters, messages):
    return {
        'e': create_action('export', 'csv', all_counters, history, messages),
        'j': create_action('export', 'json', all_counters, history, messages),
        'k': create_action('import', 'json', all_counters, history, messages),
        'q': lambda: handle_file('save', settings, counter, history, all_counters, messages)
    }

def main(stdscr):
    settings, messages, all_counters, counter, history = initialize_program_and_parse_args()

    if settings is None:
        return

    actions = initialize_actions(settings, counter, history, all_counters, messages)

    while True:
        action_key = display_and_get_input(stdscr, messages["menu"])
        execute_action_with_message(stdscr, action_key, actions, messages)
        process_and_display_notifications(stdscr, counter, settings, messages)
