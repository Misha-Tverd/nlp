# number_1 = int(input("Input first number: "))
# number_2 = int(input("Input second number : "))
# operant = input("Input operant: ")

# if operant == "+":
#     print(f"Sum of number: {number_1 + number_2}")
# elif operant == "-":
#     print(f"Difference of number: {number_1 - number_2}")
# elif operant == "*":
#     print(f"Product of number: {number_1 * number_2}")
# elif operant == "/":
#     print(f"Fraction of number: {number_1 / number_2}")
# else:
#     print("Choose correct operant")

# def calculade(a, b, op):
#     operands = {
#         "+": lambda: a + b,
#         "-": lambda: a - b,
#         "*": lambda: a * b,
#         "**": lambda: a ** b,
#         "/": lambda: "Division by zero" if b == 0 else a / b,
#         "//": lambda: "Division by zero" if b == 0 else a // b
#     }

#     if op in operands:
#         return operands[op]()
#     else:
#         return "Choose correct operant"

# number_1 = int(input("Input first number: "))
# number_2 = int(input("Input second number: "))
# operant = input("Input operant: ")

# result = calculade(number_1, number_2, operant)
# print(result)







def calculade(a, b, op):
    operant = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    return operant[op](a, b)


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return ValueError("Division by zero")
    else:
        return a / b


def get_numbers():
    while True:
        try:
            first = int(input("Input first number: "))
            second = int(input("Input second number: "))
            return first, second
        except ValueError:
            print("Input incorrect data")
    

def get_operant():
    
    list_op = ["+", "-", "/", "*"]
    while True:
        operant = input("Input operant: ")
        if operant in list_op:
            return operant
        else:
            print("Choose correct operant")

def main():

    first, second = get_numbers()
    operant = get_operant()
    
    print(calculade(first, second, operant))

main()