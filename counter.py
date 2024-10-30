# counter.py

def display_options(stdscr, program_data):
    key = stdscr.getkey()
    if key == 'r':
        reset_counter(program_data)
    elif key == 'n':
        program_data[0]["notifications"] = not program_data[0]["notifications"]

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    while True:
        process_input_action_and_notifications(stdscr, actions, program_data)
        display_options(stdscr, program_data)
        update_counter(program_data)
