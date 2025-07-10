# counter.py

from datetime import datetime
from pathlib import Path

THRESHOLD = 100

def write_file(name, content, append=False):
    path = Path(name)
    text = content + "\n"
    path.write_text((path.read_text() + text) if append and path.exists() else text)

def auto_backup(data):
    stats = data[2]
    stats["backup_count"] = stats.get("backup_count", 0) + 1
    name = f"backup_{datetime.now():%Y%m%d_%H%M%S}.txt"
    try:
        write_file(name, str(data))
        print(f"✅ Backup saved: {name}")
    except Exception as e:
        print(f"❌ Backup error: {e}")

def main(stdscr):
    data, actions = initialize_program_and_actions()
    if not data: return

    while True:
        stats = data[2]
        process_input_action_and_notifications(stdscr, actions, data)
        auto_backup(data)

        if stats.get("total", 0) > THRESHOLD:
            msg = f"⚠️ Total ({stats['total']}) > {THRESHOLD}"
            write_file("warnings.log", msg, append=True)
            print(msg)

        display_options(stdscr, data)
        update_counter_and_log(data)
