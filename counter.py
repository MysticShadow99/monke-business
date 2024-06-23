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

def main():
    counter = load_counter()
    while True:
        action = input("Enter 'i' to increment, 'd' to decrement, 'r' to reset, or 'q' to quit: ").strip().lower()
        if action == 'i':
            counter = increment(counter)
        elif action == 'd':
            counter = decrement(counter)
        elif action == 'r':
            counter = reset()
        elif action == 'q':
            save_counter(counter)
            break
        else:
            print("Invalid input.")
        print(f"Counter: {counter}")

if __name__ == "__main__":
    main()
