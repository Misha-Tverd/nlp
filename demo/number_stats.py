
numbers = input("Input a number: ")
list_numbers = []
count_numbers = 0
sum_number = 0
min_number = 999999999
max_number = 0
for i in numbers.split():
    list_numbers.append(i)
    number_int = int(i)
    if number_int < min_number:
        min_number = number_int

    if number_int > max_number:
        max_number = number_int

    count_numbers += 1
    sum_number += int(i)
    average = sum_number / count_numbers
print(list_numbers, count_numbers, sum_number, average, max_number, min_number) 
