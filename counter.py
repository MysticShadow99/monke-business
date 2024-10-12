# counter.py

def get_and_process_user_input(stdscr, actions, messages):
    action_key = display_and_get_input(stdscr, messages["menu"])
    if action_key in actions:
        actions[action_key]()
        display_content(stdscr, [action_key], 'message', messages)

def process_user_actions_and_notifications(stdscr, actions, counter, settings, messages):
    get_and_process_user_input(stdscr, actions, messages)
    generate_and_display_notifications(stdscr, counter, settings, messages)

def initialize_and_run(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    settings, messages, all_counters, counter, history = program_data

    while True:
        process_user_actions_and_notifications(stdscr, actions, counter, settings, messages)

def main(stdscr):
    initialize_and_run(stdscr)
