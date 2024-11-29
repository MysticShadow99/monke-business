# counter.py

def validate_data_integrity(program_data):
    if program_data[2]["total"] < 0:
        program_data[2]["total"] = 0

def auto_backup_data(program_data, backup_file="backup_data.txt"):
    with open(backup_file, 'w') as f:
        f.write(str(program_data))

def send_notification(message):
    print(f"Notification: {message}")

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    while True:
        process_input_action_and_notifications(stdscr, actions, program_data)
        validate_data_integrity(program_data)
        auto_backup_data(program_data)
        send_notification("Backup completed successfully.")  # Notify on backup
        display_options(stdscr, program_data)
        update_counter_and_log(program_data)
