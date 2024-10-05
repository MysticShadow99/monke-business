# counter.py

def initialize_program():
    settings, messages, all_counters, counter, history = initialize_program_and_parse_args()
    if settings is None:
        return None, None
    return settings, messages, all_counters, counter, history

def main(stdscr):
    program_data = initialize_program()
    if program_data is None:
        return

    settings, messages, all_counters, counter, history = program_data

    actions = initialize_actions(settings, counter, history, all_counters, messages)

    while True:
        handle_user_input_and_display(stdscr, messages, actions)
        process_and_display_notifications(stdscr, counter, settings, messages)
