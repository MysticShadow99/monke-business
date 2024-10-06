# counter.py

def generate_and_display_notifications(stdscr, counter, settings, messages):
    notifications = generate_notifications(counter, settings)
    process_and_display_content(stdscr, notifications, 'notification', messages)

def main(stdscr):
    program_data = initialize_program()
    if program_data is None:
        return

    settings, messages, all_counters, counter, history = program_data

    actions = initialize_actions(settings, counter, history, all_counters, messages)

    while True:
        handle_user_input_and_display(stdscr, messages, actions)
        generate_and_display_notifications(stdscr, counter, settings, messages)
