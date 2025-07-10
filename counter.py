# counter.py

import json
from datetime import datetime

THRESHOLD = 100

def main(stdscr):
    data, actions = initialize_program_and_actions()
    if not data: return

    while True:
        stats = data[2]
        process_input_action_and_notifications(stdscr, actions, data)

        stats["backup_count"] = stats.get("backup_count", 0) + 1
        with open(f"backup_{datetime.now():%Y%m%d_%H%M%S}.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        if stats.get("total", 0) > THRESHOLD:
            with open("warnings.log", 'a', encoding='utf-8') as f:
                f.write(f"⚠️ Total ({stats['total']}) > {THRESHOLD}\n")

        display_options(stdscr, data)
        update_counter_and_log(data)
