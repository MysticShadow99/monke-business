# counter.py

import json

def save_config_to_file(config, filename):
    with open(filename, "w") as config_file:
        json.dump(config, config_file, indent=4)

def load_config_from_file(filename):
    try:
        with open(filename, "r") as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        print(f"Configuration file {filename} not found.")
        return {}

# Добавим новую опцию в аргументы командной строки для сохранения настроек:
def parse_arguments():
    parser = argparse.ArgumentParser(description="Counter script with auto-save and notifications.")
    parser.add_argument("--config", type=str, help="Filename of the configuration file to load")
    parser.add_argument("--save_config", type=str, help="Filename to save current configuration")
    # ... другие аргументы ...
    return parser.parse_args()

# В основном коде добавим логику для сохранения конфигурации:
def main(stdscr):
    args = parse_arguments()
    config = load_config_from_file(args.config) if args.config else {}
    apply_command_line_args(args, config)

    if args.save_config:
        save_config_to_file(config, args.save_config)
        print(f"Configuration saved to {args.save_config}.")
        return

    # ... остальной код ...
