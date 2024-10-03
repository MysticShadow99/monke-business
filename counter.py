# counter.py

def display_content(stdscr, content, content_type, messages):
    if content_type == 'notification':
        display_notification(stdscr, content, messages)
    else:
        display_message(stdscr, content, messages)

def process_and_display_content(stdscr, content_list, content_type, messages):
    for content in content_list:
        display_content(stdscr, content, content_type, messages)

def process_and_display_notifications(stdscr, counter, settings, messages):
    notifications = generate_notifications(counter, settings)
    process_and_display_content(stdscr, notifications, 'notification', messages)

def main(stdscr):
    settings, messages, all_counters, counter, history = initialize_program_and_parse_args()

    if settings is None:
        return

    actions = initialize_actions(settings, counter, history, all_counters, messages)

    while True:
        action_key = display_and_get_input(stdscr, messages["menu"])
        execute_action_with_message(stdscr, action_key, actions, messages)
        process_and_display_notifications(stdscr, counter, settings, messages)
