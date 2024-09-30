# counter.py

def process_data_action(action, file_type, all_counters, history, messages):
    try:
        if action == 'export':
            export_data(file_type, all_counters, history)
        elif action == 'import':
            import_data(file_type, all_counters, history)
        display_action_message(stdscr, action, messages)
    except (IOError, OSError) as e:
        display_action_message(stdscr, action, messages, error=e)

def main(stdscr):
    settings, messages, all_counters, counter, history = initialize_program_and_parse_args()

    if settings is None:
        return

    actions = {
        'e': lambda: process_data_action('export', 'csv', all_counters, history, messages),
        'j': lambda: process_data_action('export', 'json', all_counters, history, messages),
        'k': lambda: process_data_action('import', 'json', all_counters, history, messages),
        'q': lambda: handle_file('save', settings, counter, history, all_counters, messages)
    }

    while True:
        action_key = display_and_get_input(stdscr, messages["menu"])
        execute_action_with_message(stdscr, action_key, actions, messages)
        process_and_display_notifications(stdscr, counter, settings, messages)
