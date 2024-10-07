# counter.py

def execute_and_display_action(stdscr, action_key, actions, messages):
    if action_key in actions:
        actions[action_key]()
        display_action_message(stdscr, action_key, messages)

def main(stdscr):
    program_data = initialize_program()
    if program_data is None:
        return

    settings, messages, all_counters, counter, history = program_data

    actions = initialize_actions(settings, counter, history, all_counters, messages)

    while True:
        action_key = display_and_get_input(stdscr, messages["menu"])
        execute_and_display_action(stdscr, action_key, actions, messages)
        generate_and_display_notifications(stdscr, counter, settings, messages)
