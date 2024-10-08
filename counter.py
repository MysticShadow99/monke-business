# counter.py

def initialize_program_and_actions():
    program_data = initialize_program()
    if program_data is None:
        return None, None

    settings, messages, all_counters, counter, history = program_data
    actions = initialize_actions(settings, counter, history, all_counters, messages)

    return program_data, actions

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    settings, messages, all_counters, counter, history = program_data

    while True:
        action_key = display_and_get_input(stdscr, messages["menu"])
        execute_and_display_action(stdscr, action_key, actions, messages)
        generate_and_display_notifications(stdscr, counter, settings, messages)
