# counter.py

def increment(counter):
    return counter + 1

def decrement(counter):
    return counter - 1

def reset():
    return 0

def main():
    counter = 0
    action = input("Enter 'i' to increment, 'd' to decrement, or 'r' to reset: ").strip().lower()
    if action == 'i':
        counter = increment(counter)
    elif action == 'd':
        counter = decrement(counter)
    elif action == 'r':
        counter = reset()
    else:
        print("Invalid input.")
    print(f"Counter: {counter}")

if __name__ == "__main__":
    main()
