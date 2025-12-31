list_numbers = [2, 3, 12, 4, 5, 22, 33, 43, 100]
list_numbers.sort()
print(list_numbers[::-1][0])
print(list_numbers[0])


sum_number = 0
for i in list_numbers:
    if i % 2 == 0:
        sum_number += 1
print(sum_number)


new_list = []
for i in list_numbers:
    if i > 10:
        new_list.append(i)
print(new_list)

