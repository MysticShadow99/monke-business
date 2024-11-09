# counter.py

def display_summary(program_data):
    print(f"Total: {program_data[2]['total']}, Max: {program_data[2]['max']}, Notifications: {program_data[0]['notifications']}")

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    while True:
        process_input_action_and_notifications(stdscr, actions, program_data)
        display_options(stdscr, program_data)
        update_counter_and_log(program_data)
        display_summary(program_data)
