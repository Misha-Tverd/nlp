

def group_first_letter(list_words):
    letter = {
    "a": [],
    "b": [],
    "c": [],
    "d": [],
    "e": [],
    "f": [],
    "g": [],
    "h": [],
    "q": [],
    "r": [],
    "t": [],
    "n": [],
    "m": [],
    "y": [],
    "u": [],
    "i": [],
    "o": [],
    "p": [],
    "s": [],
    "k": [],
    "l": [],
    "z": [],
    "x": [],
    "v": [],
    }
    for i in list_words:
        first_letter = i[0]
        first_letter = first_letter.lower()
        if first_letter.lower() in letter:
            letter[first_letter].append(i)
    return letter

print(group_first_letter(["first", "append", "second", "hi", "hello", "Then", "that"]))


def stats_dict(dictionary):
    total = 0
    avarage = 0
    maximum = 0
    quantite = 0
    for i in dictionary:
        score = i["score"]
        
        total += score
        quantite += 1
        if score > maximum:
            maximum = score
    avarage = quantite / total
    return(f"Total: {total}, avarage: {avarage}, maximum: {maximum}")
print(stats_dict([{"name": "misha", "score": 3}, {"name": "andrey", "score": 4}]))