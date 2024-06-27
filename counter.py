# counter.py
import os

def increment(counter):
    return counter + 1

def decrement(counter):
    return counter - 1

def reset():
    return 0

def save_counter(counter):
    with open("counter.txt", "w") as f:
        f.write(str(counter))

def load_counter():
    if os.path.exists("counter.txt"):
        with open("counter.txt", "r") as f:
            return int(f.read())
    else:
        return 0

def save_history(history):
    with open("history.txt", "w") as f:
        f.write("\n".join(history))

def load_history():
    if os.path.exists("history.txt"):
        with open("history.txt", "r") as f:
            return f.read().split("\n")
    else:
        return []

def main():
    if input("Would you like to set a starting value for the counter? (y/n): ").strip().lower() == 'y':
        counter = int(input("Enter the starting value for the counter: "))
    else:
        counter = load_counter()

    history = load_history()
    previous_counters = []
    all_counters = [counter]

    while True:
        action = input("Enter 'i' to increment, 'd' to decrement, 'r' to reset, 'h' to view history, 'a' to view all counter values, 'u' to undo last action, or 'q' to quit: ").strip().lower()
        if action in ['i', 'd', 'r']:
            previous_counters.append(counter)
        
        if action == 'i':
            counter = increment(counter)
            history.append("Increment")
            all_counters.append(counter)
        elif action == 'd':
            counter = decrement(counter)
            history.append("Decrement")
            all_counters.append(counter)
        elif action == 'r':
            counter = reset()
            history.append("Reset")
            all_counters.append(counter)
        elif action == 'h':
            print("History:")
            for record in history:
                print(record)
            continue  # Skip the print counter line
        elif action == 'a':
            print("All counter values:")
            for value in all_counters:
                print(value)
            continue  # Skip the print counter line
        elif action == 'u':
            if previous_counters:
                counter = previous_counters.pop()
                history.append("Undo")
                all_counters.append(counter)
            else:
                print("Nothing to undo.")
            continue  # Skip the print counter line
        elif action == 'q':
            save_counter(counter)
            save_history(history)
            break
        else:
            print("Invalid input.")
        
        print(f"Counter: {counter}")

if __name__ == "__main__":
    main()
