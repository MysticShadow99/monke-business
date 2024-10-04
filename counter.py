# counter.py

def handle_user_input_and_display(stdscr, messages, actions):
    action_key = display_and_get_input(stdscr, messages["menu"])
    execute_action_with_message(stdscr, action_key, actions, messages)

def main(stdscr):
    settings, messages, all_counters, counter, history = initialize_program_and_parse_args()

    if settings is None:
        return

    actions = initialize_actions(settings, counter, history, all_counters, messages)

    while True:
        handle_user_input_and_display(stdscr, messages, actions)
        process_and_display_notifications(stdscr, counter, settings, messages)
