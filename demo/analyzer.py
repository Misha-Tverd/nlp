import algo_utils

numbers = input("Take a list numbers: ")

list_numbers = []

for i in numbers.split():
    list_numbers.append(int(i))

max_min = algo_utils.max_min_number(list_numbers)
min, max = max_min
print(f"Here min value: {min}, here max value: {max}")

even_numbers = algo_utils.even_numbers(list_numbers)
print(f"Here sum even numbers: {even_numbers}")

list_bigger_numbers = algo_utils.numbers_greate_given_number(list_numbers)
print(f"Here bigger numbers: {list_bigger_numbers}")