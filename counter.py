# counter.py

def auto_backup_data(program_data, backup_file="backup_data.txt"):
    with open(backup_file, 'w') as f:
        f.write(str(program_data))
    print("Backup completed successfully.")  # Inline notification

def track_backup_frequency(program_data):
    if "backup_count" not in program_data[2]:
        program_data[2]["backup_count"] = 0
    program_data[2]["backup_count"] += 1

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    while True:
        process_input_action_and_notifications(stdscr, actions, program_data)
        auto_backup_data(program_data)  # Combined backup and notification
        track_backup_frequency(program_data)  # Increment backup count
        display_options(stdscr, program_data)
        update_counter_and_log(program_data)
