# counter.py

def update_counter_and_log(program_data):
    program_data[2]["total"] += 1
    program_data[2]["max"] = max(program_data[2]["total"], program_data[2]["max"])
    with open("counter_log.txt", 'a') as f:
        f.write(f"Current count: {program_data[2]['total']}, Max count: {program_data[2]['max']}\n")

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    while True:
        process_input_action_and_notifications(stdscr, actions, program_data)
        display_options(stdscr, program_data)
        update_counter_and_log(program_data)
