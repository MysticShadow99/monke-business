# counter.py

def increment(counter):
    return counter + 1

def decrement(counter):
    return counter - 1

def main():
    counter = 0
    action = input("Enter 'i' to increment or 'd' to decrement: ").strip().lower()
    if action == 'i':
        counter = increment(counter)
    elif action == 'd':
        counter = decrement(counter)
    else:
        print("Invalid input.")
    print(f"Counter: {counter}")

if __name__ == "__main__":
    main()
