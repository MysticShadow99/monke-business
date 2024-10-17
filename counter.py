# counter.py

def display_status(stdscr, program_data):
    stdscr.addstr(f"Current counter: {program_data[3]['current']}\n")
    stdscr.addstr(f"Max counter: {program_data[3]['max']}\n")

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    while True:
        process_input_action_and_notifications(stdscr, actions, program_data)
        display_status(stdscr, program_data)
