# counter.py

def parse_arguments():
    parser = argparse.ArgumentParser(description="Counter script with auto-save and notifications.")
    parser.add_argument("--config", type=str, help="Filename of the configuration file")
    parser.add_argument("--counter_file", type=str, help="Filename to save counter value")
    parser.add_argument("--history_file", type=str, help="Filename to save history")
    parser.add_argument("--all_counters_file", type=str, help="Filename to save all counter values")
    parser.add_argument("--backup_interval", type=int, help="Backup interval in seconds")
    parser.add_argument("--notification", nargs=2, action='append', help="Set notifications in the format 'value message'")
    parser.add_argument("--show_settings", action='store_true', help="Show current settings")
    parser.add_argument("--language", type=str, help="Set language for messages (en/ru)")
    parser.add_argument("--command", type=str, choices=['increment', 'decrement', 'reset', 'set'], help="Command to execute")
    parser.add_argument("--value", type=int, help="Value to set the counter to (for 'set' command)")
    parser.add_argument("--backup", action='store_true', help="Create backups of all data files")
    return parser.parse_args()

# Добавим проверку в основной функции, чтобы при наличии флага --backup скрипт создал резервные копии:
def main(stdscr):
    args = parse_arguments()
    config = load_config_from_file(args.config) if args.config else {}
    apply_command_line_args(args, config)

    if args.backup:
        backup_file(config["counter_file"], 5)
        backup_file(config["history_file"], 5)
        backup_file(config["all_counters_file"], 5)
        print("Backup completed.")
        return

    language = config.get("language", "en")
    messages = load_messages(language)
    counter_file = config.get("counter_file", "counter.txt")
    history_file = config.get("history_file", "history.txt")
    all_counters_file = config.get("all_counters_file", "all_counters.txt")
    backup_interval = config.get("backup_interval", 600)
    notifications = config.get("notifications", {})

    settings = {"counter_file": counter_file, "history_file": history_file, "all_counters_file": all_counters_file, "backup_interval": backup_interval, "notifications": notifications, "language": language}
    ...
