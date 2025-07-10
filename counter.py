# counter.py

import json
from datetime import datetime
from pathlib import Path

THRESHOLD = 100

def write_file(path, content, append=False, as_json=False):
    mode = 'a' if append else 'w'
    with open(path, mode, encoding='utf-8') as f:
        if as_json:
            json.dump(content, f, ensure_ascii=False, indent=2)
        else:
            f.write(content + "\n")

def auto_backup(data):
    data[2]["backup_count"] = data[2].get("backup_count", 0) + 1
    name = f"backup_{datetime.now():%Y%m%d_%H%M%S}.json"
    try:
        write_file(name, data, as_json=True)
    except Exception as e:
        write_file("warnings.log", f"❌ Backup error: {e}", append=True)

def main(stdscr):
    data, actions = initialize_program_and_actions()
    if not data: return

    while True:
        stats = data[2]
        process_input_action_and_notifications(stdscr, actions, data)
        auto_backup(data)

        if stats.get("total", 0) > THRESHOLD:
            write_file("warnings.log", f"⚠️ Total ({stats['total']}) > {THRESHOLD}", append=True)

        display_options(stdscr, data)
        update_counter_and_log(data)
