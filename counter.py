# counter.py

import json
from datetime import datetime
from pathlib import Path

THRESHOLD = 100

def auto_backup(data):
    data[2]["backup_count"] = data[2].get("backup_count", 0) + 1
    fname = f"backup_{datetime.now():%Y%m%d_%H%M%S}.json"
    Path(fname).write_text(json.dumps(data, ensure_ascii=False, indent=2))

def log_warning(msg):
    Path("warnings.log").write_text(
        Path("warnings.log").read_text() + msg + "\n"
        if Path("warnings.log").exists() else msg + "\n"
    )

def main(stdscr):
    data, actions = initialize_program_and_actions()
    if not data: return

    while True:
        stats = data[2]
        process_input_action_and_notifications(stdscr, actions, data)
        auto_backup(data)
        if stats.get("total", 0) > THRESHOLD:
            log_warning(f"⚠️ Total ({stats['total']}) > {THRESHOLD}")
        display_options(stdscr, data)
        update_counter_and_log(data)
