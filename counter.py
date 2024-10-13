# counter.py

def display_content(stdscr, content_list, messages):
    for content in content_list:
        stdscr.addstr(f"{messages[content]}\n")

def generate_and_display_notifications(stdscr, counter, settings, messages):
    notifications = generate_notifications(counter, settings)
    display_content(stdscr, notifications, messages)

def execute_and_display_action(stdscr, action_key, actions, messages):
    if action_key in actions:
        actions[action_key]()
        display_content(stdscr, [action_key], messages)

def process_input_and_action(stdscr, actions, messages):
    action_key = display_and_get_input(stdscr, messages["menu"])
    execute_and_display_action(stdscr, action_key, actions, messages)

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    settings, messages, all_counters, counter, history = program_data

    while True:
        process_input_and_action(stdscr, actions, messages)
        generate_and_display_notifications(stdscr, counter, settings, messages)
