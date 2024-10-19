# counter.py

def execute_action(stdscr, action_key, actions, messages):
    if action_key in actions:
        actions[action_key]()
        display_content(stdscr, [action_key], messages)

def process_input_action_and_notifications(stdscr, actions, program_data):
    action_key = display_and_get_input(stdscr, program_data[1]["menu"])
    execute_action(stdscr, action_key, actions, program_data[1])

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    while True:
        process_input_action_and_notifications(stdscr, actions, program_data)
