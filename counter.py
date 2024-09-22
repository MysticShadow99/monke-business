# counter.py

def handle_data_action(action, format, all_counters, history, messages):
    try:
        if action == 'export':
            export_data(format, all_counters, history)
        elif action == 'import':
            import_data(format, all_counters, history)
        else:
            action = 'invalid'
        display_message(stdscr, generate_message(action, messages), messages)
    except Exception as e:
        display_message(stdscr, f"{generate_message('file_error', messages)}: {str(e)}", messages)

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
