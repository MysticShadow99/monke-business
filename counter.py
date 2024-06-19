# counter.py

def increment(counter):
    return counter + 1

def decrement(counter):
    return counter - 1

def main():
    counter = 0
    counter = increment(counter)
    counter = decrement(counter)
    print(f"Counter: {counter}")

if __name__ == "__main__":
    main()
