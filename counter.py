# counter.py

def load_config_with_args(args):
    config = load_and_apply_config(args)
    settings = manage_settings(config, "load")

    if args.show_settings:
        show_settings(config)
        return None
    return settings

def main(stdscr):
    args = parse_arguments()
    settings = load_config_with_args(args)

    if settings is None:
        return

    messages = load_messages(settings["language"])

    actions = {
        'e': lambda: handle_data_operation('export', 'csv', all_counters, history, messages),
        'j': lambda: handle_data_operation('export', 'json', all_counters, history, messages),
        'k': lambda: handle_data_operation('import', 'json', all_counters, history, messages),
        'q': lambda: handle_file_operations("save", settings, counter, history, all_counters)
    }

    while True:
        if not handle_user_input(stdscr, messages, actions):
            break

        process_and_display_notifications(stdscr, counter, settings, messages)
