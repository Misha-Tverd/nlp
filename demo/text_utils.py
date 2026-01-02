def stats_word(dict_words):
    word_frequency = {}

    for word in dict_words.split():
        if word not in word_frequency:
            word_frequency[word] = 1 
        else:
            word_frequency[word] += 1
    print(word_frequency)

    most_common_word = {}
    most_significant = 0
    print("\nBelow is a list of words and their frequency.\n")
    for key, value in word_frequency.items():
        print(f"That key: {key}, that value: {value}")
        if value > most_significant:
            most_common_word[key] = value
            most_significant = value
    print(f"Most common word, {most_common_word}")

    return most_common_word

