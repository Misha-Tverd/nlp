def clear_list(some_list):
    new_list = []
    for i in some_list:
        if i not in new_list:
            try:
                i = int(i)
                new_list.append(i)
                print(i)
            except ValueError:
                print(f"Value can be a str: {i}")
    print(new_list)    
        
        

clear_list([2, 2, 3, "r", 3])


def even_numbers(list_numbers):
    new_list = []
    for i in list_numbers:
        if i % 2 == 0:
            new_list.append(i * 2)
    print(new_list)

even_numbers([2, 2, 3, 1, 43, 22, 34])