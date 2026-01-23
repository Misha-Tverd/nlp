import config

def main(text):
    if config.DEFAULT_MODE = "numbers":
        list_numbers = convert_str(text)
        return stats_list_int(list_numbers)
    elif config.DEFAULT_MODE = "text":
        new_list = convert_str_to_int(text)
        stat_list = list_stats_word(new_list)
        return stat_dict

def convert_str(text):
    new_list = []
    errors = []
    for i in text.split():
        try:
            i = int(i)
            new_list.append(i)
        except ValueError:
            errors.append(i)
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
    return [count, summary, minimum, maximum, avarege]
    

def convert_str_to_int(text):
    new_list = []
    errors = ""
    for i in text.split():
        try:
            i = int(i)
            new_list.append(i)
        except ValueError:
            erros += (f"The value of \"{i}\" was not a number, so it was not preserved. \n")
    return new_list
        


def list_stats_word(some_list):
    
    word_frequency = {}
    for word in some_list.split():
       word_frequency[word] = word_frequency.get(word, 0) + 1

    most_common_words = []
    max_count = 0
    for word, count in word_frequency.items():
        if count > max_count:
            max_count = count
            most_common_words = [word]
        elif count == max_count:
            most_common_words.append(word)
    
    return {
        "words": most_common_words,
        "count": max_count
    }

    return stats
    
