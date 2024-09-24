# counter.py

def process_user_action(stdscr, actions, messages):
    action_key = display_and_get_input(stdscr, messages["menu"])
    if action_key in actions:
        execute_action(stdscr, action_key, actions, messages)
    else:
        display_message(stdscr, generate_message('invalid', messages), messages)

def main(stdscr):
    args = parse_arguments()
    counter, history, all_counters = {}, [], {}

    settings, messages, all_counters = initialize_program(args, counter, history, all_counters)
    if settings is None:
        return

    actions = {
        'e': lambda: handle_data_action('export', 'csv', all_counters, history, messages),
        'j': lambda: handle_data_action('export', 'json', all_counters, history, messages),
        'k': lambda: handle_data_action('import', 'json', all_counters, history, messages),
        'q': lambda: handle_file('save', settings, counter, history, all_counters, messages)
    }

    while True:
        process_user_action(stdscr, actions, messages)
        process_and_display_notifications(stdscr, counter, settings, messages)
