def get_numbers(numbers):
    list_numbers = []
    for i in numbers.split():
        try:
            i = int(i)
            list_numbers.append(i)
        except ValueError:
            print(f"This value: {i} will not be saved because it is not a number")
    return list_numbers

def stat_list_numbers(list_numbers):
    dict_stat = {
        "count": 0,
        "sum": 0,
        "min": list_numbers[0],
        "max": list_numbers[0],
        "average": 0
    }
    
    for value in list_numbers:
        
        dict_stat["count"] += 1
        dict_stat["sum"] += value
        if value < dict_stat["min"]:
            dict_stat["min"] = value
        elif value > dict_stat["max"]:
            dict_stat["max"] = value 
    dict_stat["average"] = dict_stat["sum"] / dict_stat["count"]
    return dict_stat
