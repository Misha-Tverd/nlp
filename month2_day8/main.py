def parse_numbers(text) -> list:
    # Convert a string of space-separated values into a list of integers, ignoring non-integer values.
    new_list = []
    errors = []
    if text == "" or text == None:
        new_list.append("empty")
        return new_list, False
    for i in text.split():
        try:
            i = int(i)
            new_list.append(i)
            errors = False
        except ValueError:
            errors = True
    return new_list, errors

def main():
    list_number, errors = parse_numbers("")
    print("number list:", list_number)
    print("errors:", errors)
main()
