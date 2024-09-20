# counter.py

def generate_message(action, messages):
    message_mapping = {
        'export': "data_exported",
        'import': "data_imported",
        'save': "data_saved",
        'invalid': "invalid_input",
        'file_error': "file_error"
    }
    return messages.get(message_mapping.get(action, "invalid"))

def handle_file(action, settings, counter, history, all_counters, messages):
    try:
        if action == 'save':
            save_data(settings, counter, history, all_counters)
        elif action == 'load':
            load_data(settings, counter, history, all_counters)
        else:
            action = 'invalid'
        display_message(stdscr, generate_message(action, messages), messages)
    except (IOError, OSError) as e:
        display_message(stdscr, f"{generate_message('file_error', messages)}: {str(e)}", messages)

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
