import numbers
import text

def main():
    menu = """ Choose mode:
    1. Numbers
    2. Text """
    print(menu)
    menu_item = int(input(">> "))
    if menu_item == 1:
        input_numbers = input("Input numbers, example(3 2 4 1 32): \n")
        list_numbers = numbers.get_numbers(input_numbers)
        stat_numbers = numbers.stat_list_numbers(list_numbers)
        return stat_numbers
    elif menu_item == 2:
        some_text = input("Input some text: ")
        stat_text = text.word_frequency_dictionary(some_text)
        return stat_text
    else:
        return "Choose correct menu item"
    
print(main())

