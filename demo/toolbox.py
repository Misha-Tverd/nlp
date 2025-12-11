def is_even(n):
    return False if n % 2 else True


def count_vowels(text):
    list_vowels = ["a", "e", "i", "o", "u", "y"]
    count = 0
    
    for i in text:
        if i in list_vowels:
            count += 1
    return count


def reverse_text(text):
    return text[::-1]

print(is_even(5))
print(count_vowels("Helli"))
print(reverse_text("Thanks"))