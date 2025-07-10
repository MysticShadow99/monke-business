# counter.py

import datetime

CRITICAL_THRESHOLD = 100

def auto_backup_data(program_data, backup_file_prefix="backup_data"):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"{backup_file_prefix}_{timestamp}.txt"
    try:
        with open(backup_file, 'w') as f:
            f.write(str(program_data))
        program_data_section = program_data[2]
        program_data_section["backup_count"] = program_data_section.get("backup_count", 0) + 1
        print(f"Backup completed successfully to {backup_file}.")  # Inline notification
    except Exception as e:
        print(f"Backup failed: {e}")

def main(stdscr):
    program_data, actions = initialize_program_and_actions()
    if program_data is None:
        return

    while True:
        process_input_action_and_notifications(stdscr, actions, program_data)
        auto_backup_data(program_data)

        total = program_data[2]["total"]
        if total > CRITICAL_THRESHOLD:
            warning = f"Warning: Total ({total}) exceeds the critical threshold!"
            with open("warnings.log", 'a') as log_file:
                log_file.write(warning + "\n")
            print(warning)

        display_options(stdscr, program_data)
        update_counter_and_log(program_data)
