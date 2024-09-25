# counter.py

def display_action_message(stdscr, action, messages, error=None):
    if error:
        display_message(stdscr, f"{generate_message('file_error', messages)}: {str(error)}", messages)
    else:
        display_message(stdscr, generate_message(action, messages), messages)

def handle_file(action, settings, counter, history, all_counters, messages):
    try:
        result = process_data(action, settings, counter, history, all_counters)
        if result is not True:
            display_action_message(stdscr, 'invalid', messages)
        else:
            display_action_message(stdscr, action, messages)
    except (IOError, OSError) as e:
        display_action_message(stdscr, action, messages, error=e)

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
