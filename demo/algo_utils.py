def max_min_number(list_numbers):
    min_number = 0
    max_number = 0
    for i in list_numbers:
        if i > max_number:
            max_number = i
        if min_number == 0 or min_number > i:
            min_number = i

    return min_number, max_number




def even_numbers(list_numbers):
    list_even_numbers = 0
    for i in list_numbers:
        if i % 2 == 0:
            list_even_numbers += i
    return list_even_numbers





def numbers_greate_given_number(list_numbers):
    parametr_func = 32
    list_bigger_numbers = []
    for i in list_numbers:
        if i > parametr_func:
            list_bigger_numbers.append(i)
    return list_bigger_numbers

