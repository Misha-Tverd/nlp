

allowed = "+-/*"
def val_value():
    while True:
        some_str = input("Enter the value: ")
        if some_str in allowed and len(some_str) == 1:
            return True
        else:
            print("Enter valid value")

print(val_value())

def devine(first, second):
    if second != 0:
        raise ValueError("You cannot divide by zero")
    else:
        return True

def main():
    val_value()


if __name__ == "__main__":
    main()