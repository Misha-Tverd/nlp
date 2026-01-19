import file_utils
import data_utils



def main():
    menu_list = """ Choose mode:
    1 - read numbers from file
    2 - write result to file
    """
    menu = int(input(f"{menu_list} \n>>: "))
    if menu == 1:
        text = file_utils.read_text_file("input.txt")
        list_numbers = data_utils.convect_str(text)
        stats = data_utils.stat_list_int(list_numbers)
        result = ""
        for key, value in stats.items():
            result += f"{key}: {value}\n"
        print(result)

        # for value in statistic:
        #     print(f"Its {key} and his {value}\n")
    elif menu == 2:
        text = file_utils.read_text_file("input.txt")
        list_numbers = data_utils.convect_str(text)
        statistic = data_utils.stat_list_int(list_numbers)
        with open("output.txt", "w", encoding="utf-8") as file:
            for key, value in statistic.items():
                file.write(f"{key}: {value}\n")
    else:
        print("Something wrong")

main()