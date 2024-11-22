# counter.py

def validate_data_integrity(program_data):
    if program_data[2]["total"] < 0:
        program_data[2]["total"] = 0

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    archive_log()  # Archive log at the start of the program

    while True:
        process_input_action_and_notifications(stdscr, actions, program_data)
        validate_data_integrity(program_data)  # Validate data
        display_options(stdscr, program_data)
        update_counter_and_log(program_data)
