# counter.py

def process_data(action, settings, counter, history, all_counters):
    try:
        if action == 'save':
            save_data(settings, counter, history, all_counters)
        elif action == 'load':
            load_data(settings, counter, history, all_counters)
        else:
            return False
        return True
    except (IOError, OSError) as e:
        return f"file_error: {str(e)}"

def handle_file(action, settings, counter, history, all_counters, messages):
    result = process_data(action, settings, counter, history, all_counters)
    if result is True:
        display_message(stdscr, generate_message(action, messages), messages)
    elif isinstance(result, str):
        display_message(stdscr, result, messages)
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
        action_key = display_and_get_input(stdscr, messages["menu"])
        execute_action(stdscr, action_key, actions, messages)
        process_and_display_notifications(stdscr, counter, settings, messages)
