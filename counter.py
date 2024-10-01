# counter.py

def display_notification_or_message(stdscr, content, is_notification, messages):
    if is_notification:
        display_notification(stdscr, content, messages)
    else:
        display_message(stdscr, content, messages)

def process_and_display_notifications(stdscr, counter, settings, messages):
    notifications = generate_notifications(counter, settings)
    for notification in notifications:
        display_notification_or_message(stdscr, notification, True, messages)

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
