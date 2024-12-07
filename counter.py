# counter.py

def auto_backup_data(program_data, backup_file="backup_data.txt"):
    with open(backup_file, 'w') as f:
        f.write(str(program_data))
    program_data[2]["backup_count"] = program_data[2].get("backup_count", 0) + 1
    print("Backup completed successfully.")  # Inline notification

def summarize_data(program_data):
    summary = f"Total: {program_data[2]['total']}, Backups: {program_data[2].get('backup_count', 0)}"
    print(summary)
    with open("summary.log", 'a') as log_file:
        log_file.write(summary + "\n")

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    while True:
        process_input_action_and_notifications(stdscr, actions, program_data)
        auto_backup_data(program_data)
        if program_data[2]["total"] > 100:
            warning = f"Warning: Total ({program_data[2]['total']}) exceeds the critical threshold!"
            with open("warnings.log", 'a') as log_file:
                log_file.write(warning + "\n")
            print(warning)
        summarize_data(program_data)  # Add daily data summary
        display_options(stdscr, program_data)
        update_counter_and_log(program_data)
