# while True:
#     try:
#         input_number = int(input("Input some number: "))
#         break
#     except ValueError:
#         print("\nInput some number not a text")
    
# print(input_number)

def get_numbers():
    while True:
        try:
            user_input = input("Enter numbers separated by spaces: ")
            numbers = [int(x) for x in user_input.split()]
            return numbers
        except ValueError:
            print("Input always numbers")

print(get_numbers())