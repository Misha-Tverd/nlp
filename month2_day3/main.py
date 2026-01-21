import config
import numbers
import file_utils
from pathlib import Path

def main():
    BASE_DIR = Path(__file__).resolve().parent.parent

    if config.DEFAULT_MODE == "numbers":
        data_file = BASE_DIR / "month2_day2" / "input.txt"
        text_from_file = file_utils.read_text_file(data_file)
        numbers_list = numbers.convert_str(text_from_file)
        stats_numbers = numbers.stat_list_int(numbers_list)
    print(stats_numbers)
    if config.SAVE_TO_FILE == True:
        data_file = BASE_DIR / "month2_day2" / "output.txt"
       
        with open(data_file, "w", encoding="utf-8") as file:
            for key, value in stats_numbers.items():
                file.write(f"{key} : {value}\n")
                print(key, value)
main()