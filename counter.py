# counter.py

def apply_command_line_args(args, config):
    if args.counter_file: config["counter_file"] = args.counter_file
    if args.history_file: config["history_file"] = args.history_file
    if args.all_counters_file: config["all_counters_file"] = args.all_counters_file
    if args.backup_interval: config["backup_interval"] = args.backup_interval
    if args.notification: config["notifications"] = {int(k): v for k, v in args.notification}
    if args.language: config["language"] = args.language

# Теперь заменим проверки в основном коде на вызов этой функции:
def main(stdscr):
    args = parse_arguments()
    config = load_config_from_file(args.config) if args.config else {}
    apply_command_line_args(args, config)
    language = config.get("language", "en")
    messages = load_messages(language)
    counter_file = config.get("counter_file", "counter.txt")
    history_file = config.get("history_file", "history.txt")
    all_counters_file = config.get("all_counters_file", "all_counters.txt")
    backup_interval = config.get("backup_interval", 600)
    notifications = config.get("notifications", {})

    settings = {"counter_file": counter_file, "history_file": history_file, "all_counters_file": all_counters_file, "backup_interval": backup_interval, "notifications": notifications, "language": language}
    ...
