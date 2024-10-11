# counter.py

def display_content(stdscr, content_list, content_type, messages):
    for content in content_list:
        if content_type == 'notification':
            display_notification(stdscr, content, messages)
        else:
            display_message(stdscr, content, messages)

def generate_and_display_notifications(stdscr, counter, settings, messages):
    notifications = generate_notifications(counter, settings)
    display_content(stdscr, notifications, 'notification', messages)

def execute_and_display_action(stdscr, action_key, actions, messages):
    if action_key in actions:
        actions[action_key]()
        display_content(stdscr, [action_key], 'message', messages)

def process_user_actions_and_notifications(stdscr, actions, counter, settings, messages):
    action_key = display_and_get_input(stdscr, messages["menu"])
    execute_and_display_action(stdscr, action_key, actions, messages)
    generate_and_display_notifications(stdscr, counter, settings, messages)

def main(stdscr):
    initialize_and_run(stdscr)
