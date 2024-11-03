# counter.py

def load_settings(file_name="settings.json"):
    import json
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"notifications": True}

def initialize_program_and_actions():
    settings = load_settings()
    messages = {"action_1": "Action 1 executed", "menu": "Select an action:"}
    counter = {"total": 0, "current": 0, "max": 0}
    actions = {"action_1": lambda: None}
    return [settings, messages, counter], actions

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    while True:
        process_input_action_and_notifications(stdscr, actions, program_data)
        display_options(stdscr, program_data)
        update_counter(program_data)
