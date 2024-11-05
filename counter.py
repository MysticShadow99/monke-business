# counter.py

def log_counter_state(counter, log_file="counter_log.txt"):
    with open(log_file, 'a') as f:
        f.write(f"Current count: {counter['total']}, Max count: {counter['max']}\n")

def update_counter_and_log(program_data):
    program_data[2]["total"] += 1
    program_data[2]["max"] = max(program_data[2]["total"], program_data[2]["max"])
    log_counter_state(program_data[2])

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    while True:
        process_input_action_and_notifications(stdscr, actions, program_data)
        display_options(stdscr, program_data)
        update_counter_and_log(program_data)
