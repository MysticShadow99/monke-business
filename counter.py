# counter.py

def initialize_and_run(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    settings, messages, all_counters, counter, history = program_data

    while True:
        process_user_actions_and_notifications(stdscr, actions, counter, settings, messages)

def main(stdscr):
    initialize_and_run(stdscr)
