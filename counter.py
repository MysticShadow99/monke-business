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
    counter = load_counter()
    history = load_history()
    while True:
        action = input("Enter 'i' to increment, 'd' to decrement, 'r' to reset, 'h' to view history, or 'q' to quit: ").strip().lower()
        if action == 'i':
            counter = increment(counter)
            history.append("Increment")
        elif action == 'd':
            counter = decrement(counter)
            history.append("Decrement")
        elif action == 'r':
            counter = reset()
            history.append("Reset")
        elif action == 'h':
            print("History:")
            for record in history:
                print(record)
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
