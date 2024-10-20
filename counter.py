# counter.py

def save_counter_state(counter, file_name="counter_state.json"):
    import json
    with open(file_name, 'w') as f:
        json.dump(counter, f)

def update_counter_and_save(stdscr, program_data):
    program_data[3]['total'] += 1
    save_counter_state(program_data[3])

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    while True:
        process_input_action_and_notifications(stdscr, actions, program_data)
        update_counter_and_save(stdscr, program_data)
