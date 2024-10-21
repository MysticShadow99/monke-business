# counter.py

def update_counter(program_data):
    program_data[3]['total'] += 1

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    while True:
        process_input_action_and_notifications(stdscr, actions, program_data)
        update_counter(program_data)
