# counter.py

def archive_log(file_name="counter_log.txt", archive_file="archive_log.txt"):
    import shutil
    shutil.copyfile(file_name, archive_file)
    with open(file_name, 'w') as f:
        f.write("")  # Clear the original log file after archiving

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    archive_log()  # Archive log at the start of the program

    while True:
        process_input_action_and_notifications(stdscr, actions, program_data)
        display_options(stdscr, program_data)
        update_counter_and_log(program_data)
        log_summary(program_data)
