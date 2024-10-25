# counter.py

def reset_counter(program_data):
    program_data[3]['total'] = 0

def display_reset_option(stdscr, program_data):
    if stdscr.getkey() == 'r':
        reset_counter(program_data)

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    while True:
        process_input_action_and_notifications(stdscr, actions, program_data)
        display_reset_option(stdscr, program_data)
        update_counter(program_data)
