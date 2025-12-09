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

def calculade(a, b, op):
    operands = {
        "+": a + b,
        "-": a - b,
        "*": a * b,
        "/": a / b
    }

    if op in operands:
        return operands[op]
    else:
        return "Choose correct operant"

number_1 = int(input("Input first number: "))
number_2 = int(input("Input second number: "))
operant = input("Input operant: ")

result = calculade(number_1, number_2, operant)
print(result)