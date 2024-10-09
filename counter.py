# counter.py

def process_user_actions_and_notifications(stdscr, actions, counter, settings, messages):
    action_key = display_and_get_input(stdscr, messages["menu"])
    execute_and_display_action(stdscr, action_key, actions, messages)
    generate_and_display_notifications(stdscr, counter, settings, messages)

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    settings, messages, all_counters, counter, history = program_data

    while True:
        process_user_actions_and_notifications(stdscr, actions, counter, settings, messages)
