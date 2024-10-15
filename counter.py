# counter.py

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    while True:
        process_input_action_and_notifications(
            stdscr, 
            actions, 
            program_data[3],  # counter
            program_data[0],  # settings
            program_data[1]   # messages
        )
