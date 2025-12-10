# n = 1

# while True:
#     if not n % 2: 
#         print("Number: ", n)
#     n += 1
#     if n == 21:
#         break

# while True:
#     age = int(input("Input your age: "))
#     if age > 120 or age < 0:
#         print("\nInpur correct age")
#     else:
#         print("Your age: ", age)
#         break

# while True:
#     words = str(input("Something: "))
#     if words.lower() == "stop":
#         break
#     elif words.isdigit():
#         print("\nInput only words!!!")
#         continue
#     elif words == "":
#         print("Input something: ")
#         continue
#     elif words.isalpha():
#         print("correct choise")
#         break

import random

random_number = random.randint(1, 10)
n = 0
while True:
    print("Try to guess the number that the computer has chosen.")
    number = int(input("Input number: "))
    
    n += 1
    if random_number > number:
        print("More")
    elif random_number < number:
        print("Less")
    else:
        print("Correct choise, you win")
        print(f"You guessed right on the {n} try")
        break
    
    


# for n in range(2, 21, 3):
#     print("Number: ", n)