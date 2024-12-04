# counter.py

def auto_backup_data(program_data, backup_file="backup_data.txt"):
    with open(backup_file, 'w') as f:
        f.write(str(program_data))
    program_data[2]["backup_count"] = program_data[2].get("backup_count", 0) + 1
    print("Backup completed successfully.")  # Inline notification

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    while True:
        process_input_action_and_notifications(stdscr, actions, program_data)
        auto_backup_data(program_data)
        if program_data[2]["total"] > 100:  # Inline critical threshold check
            print("Warning: Total exceeds the critical threshold!")
        display_options(stdscr, program_data)
        update_counter_and_log(program_data)
