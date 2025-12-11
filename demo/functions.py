def greet(name):
    while True:
        if name.isalpha():
            break
        else:
            return "input correct name"

    return print(f"Hello, {name}")

def is_adult(age):
    if 0 > age < 120:
        return ValueError("Incorrect age, try again")
    elif age < 18:
        return "You are so young"
    elif age > 18:
        return "Your like a adult"
    

def year_of_birth(age):
    return 2025 - age

def main():
    name = input("Name: ")
    age = int(input("Age: "))

    greet(name)
    print("Adult:", is_adult(age))
    print("Born in:", year_of_birth(age))


main()