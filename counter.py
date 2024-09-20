# counter.py

def handle_file(action, settings, counter, history, all_counters, messages):
    try:
        if action == 'save':
            save_data(settings, counter, history, all_counters)
            display_message(stdscr, "data_saved", messages)
        elif action == 'load':
            load_data(settings, counter, history, all_counters)
            display_message(stdscr, "data_loaded", messages)
        else:
            display_message(stdscr, "invalid_input", messages)
    except (IOError, OSError) as e:
        display_message(stdscr, f"file_error: {str(e)}", messages)

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
        'q': lambda: handle_file('save', settings, counter, history, all_counters, messages)
    }

    while True:
        action_key = display_and_get_input(stdscr, messages["menu"])
        execute_action(stdscr, action_key, actions, messages)
        process_and_display_notifications(stdscr, counter, settings, messages)
