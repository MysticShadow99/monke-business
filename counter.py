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

def process_input_action_and_notifications(stdscr, actions, program_data):
    action_key = display_and_get_input(stdscr, program_data[1]["menu"])
    execute_and_display_action(stdscr, action_key, actions, program_data[1])

    notifications = generate_notifications(program_data[3], program_data[0])
    display_content(stdscr, notifications, program_data[1])

def display_summary(stdscr, program_data):
    stdscr.addstr(f"Total actions: {program_data[3]['total']}\n")
    stdscr.addstr(f"Notifications enabled: {program_data[0]['notifications']}\n")

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    while True:
        process_input_action_and_notifications(stdscr, actions, program_data)
