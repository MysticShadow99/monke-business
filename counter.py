# counter.py

import datetime

CRITICAL_THRESHOLD = 100

def auto_backup_data(data, backup_prefix="backup_data"):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{backup_prefix}_{timestamp}.txt"
    try:
        with open(filename, 'w') as f:
            f.write(str(data))
        stats = get_program_stats(data)
        stats["backup_count"] = stats.get("backup_count", 0) + 1
        print(f"✅ Backup saved to {filename}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def log_warning(message, log_file="warnings.log"):
    with open(log_file, 'a') as f:
        f.write(message + "\n")
    print(message)

def get_program_stats(data):
    return data[2]  # Could be replaced with better structure later

def main(stdscr):
    data, actions = initialize_program_and_actions()
    if data is None:
        return

    while True:
        process_input_action_and_notifications(stdscr, actions, data)
        auto_backup_data(data)

        stats = get_program_stats(data)
        if stats.get("total", 0) > CRITICAL_THRESHOLD:
            warning_msg = f"⚠️ Warning: Total ({stats['total']}) exceeds critical threshold!"
            log_warning(warning_msg)

        display_options(stdscr, data)
        update_counter_and_log(data)
