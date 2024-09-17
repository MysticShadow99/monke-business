# counter.py

def handle_file(action, settings, counter, history, all_counters):
    if action == 'save':
        save_data(settings, counter, history, all_counters)
        display_message(stdscr, "data_saved", messages)
    elif action == 'load':
        load_data(settings, counter, history, all_counters)
        display_message(stdscr, "data_loaded", messages)
    else:
        display_message(stdscr, "invalid_input", messages)

def main(stdscr):
    args = parse_arguments()
    settings = load_config_with_args(args)

    if settings is None:
        return

    messages = load_messages(settings["language"])

    actions = {
        'e': lambda: handle_data('export', 'csv', all_counters, history, messages),
        'j': lambda: handle_data('export', 'json', all_counters, history, messages),
        'k': lambda: handle_data('import', 'json', all_counters, history, messages),
        'q': lambda: handle_file('save', settings, counter, history, all_counters)
    }

    while True:
        handle_input_and_notifications(stdscr, messages, actions, counter, settings)
