name = input("Enter your name: ")
age = int(input("Enter your age: "))


def data_born(age):
    return print(f"You were born in {2025 - age}")
def result(name, age):
    print("\n--- RESULT ---")
    print("Name:", name)
    print("Age:", age)

if 0 < age < 18:
    print("You are underage")
    data_born(age)
    result(name, age)
elif 120 > age >= 18:
    print("You are adult")
    data_born(age)
    result(name, age)
else:
    print("Invalid age.\n Input correct age!")

