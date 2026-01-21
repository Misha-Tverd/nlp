
def convert_str(some_list):
    new_list = []
    errors = []
    for i in some_list.split():
        try:
            i = int(i)
            new_list.append(i)
        except ValueError:
            errors.append(i)
    # stat_list = stat_list_int(new_list)
    return new_list


def stat_list_int(some_list):
    
    count = 0
    summary = 0 
    minimum = some_list[0]
    maximum = 0
    avarege = 0
    for i in some_list:
        count += 1
        summary += i
        if i < minimum:
            minimum = i
        elif i > maximum:
            maximum = i 
    avarege = summary / count
    stats = {
        "count": count,
        "summary": summary,
        "minimun": minimum,
        "maximum": maximum,
        "avarage": avarege
    }
    return stats
    
