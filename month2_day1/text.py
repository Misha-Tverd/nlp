def word_frequency_dictionary(some_text):
    word_frequency = {}
    for word in some_text.split():
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
