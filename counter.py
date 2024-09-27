# counter.py

def handle_errors(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except (IOError, OSError) as e:
        return f"file_error: {str(e)}"
    except Exception as e:
        return f"error: {str(e)}"

def handle_file(action, settings, counter, history, all_counters, messages):
    result = handle_errors(process_data, action, settings, counter, history, all_counters)
    if isinstance(result, str):
        display_action_message(stdscr, action, messages, error=result)
    else:
        display_action_message(stdscr, action, messages)

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
        process_user_action(stdscr, actions, messages)
        process_and_display_notifications(stdscr, counter, settings, messages)
