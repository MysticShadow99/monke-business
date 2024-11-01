# counter.py

def save_settings(settings, file_name="settings.json"):
    import json
    with open(file_name, 'w') as f:
        json.dump(settings, f)

def toggle_notifications_and_save(program_data):
    program_data[0]["notifications"] = not program_data[0]["notifications"]
    save_settings(program_data[0])

def display_options(stdscr, program_data):
    key = stdscr.getkey()
    if key == 'r':
        reset_counter(program_data)
    elif key == 'n':
        toggle_notifications_and_save(program_data)

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    while True:
        process_input_action_and_notifications(stdscr, actions, program_data)
        display_options(stdscr, program_data)
        update_counter(program_data)
