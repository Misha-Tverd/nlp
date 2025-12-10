def data_born(age):
    return print(f"You were born in {2025 - age}")

def result(name, age):
    print("\n--- RESULT ---")
    print("Name:", name)
    print("Age:", age)

def validate_name(name):
    while True:
        if not name.isalpha():
            print("\n!!!Input only letter!!!\n")
            return False
        elif len(name) < 2:
            print("Write correct name")
            return False
        return True

def validate_age(age):
    while True:
        if 0 < age < 18:
            print("You are underage")
            return True
        elif 120 > age >= 18:
            print("You are adult")
            return True
        else:
            print("Invalid age.\n Input correct age!")
            return False

while True:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    
    if not validate_name(name):
        continue

    if not validate_age(age):
        continue
    
    data_born(age)
    result(name, age)
    break
    

