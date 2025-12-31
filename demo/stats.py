# with open("data.txt", "r") as f:
#     lines = 0
   
#     for _ in f:
#         lines += 1
#     print(lines)
#     f = f.read().split("")
#     print(f)    
import json


with open("data.txt", "r", encoding="utf-8") as f:
    lines_list = f.readlines()
print(lines_list)
full_text = "".join(lines_list)
print(full_text)
lines_count = len(lines_list)
words_count = len(full_text.split())
print(lines_count," ", words_count)
chars_count = len(full_text.replace(" ", "").replace("\n", ""))
print(chars_count)

result = {
    "lines": lines_count,
    "words": words_count,
    "chars": chars_count
}    

with open("stats.json", "w", encoding="utf-8") as f:
    json.dump(result, f)



# import json

# # 1. Читаємо дані з файлу
# with open('data.txt', 'r', encoding='utf-8') as f:
#     lines_list = f.readlines()

# # Об'єднуємо список рядків у один великий текст для зручності підрахунку
# full_text = "".join(lines_list)

# # 2. Рахуємо показники
# lines_count = len(lines_list)
# words_count = len(full_text.split())

# # Використовуємо підказку: прибираємо пробіли та переноси рядків (\n), щоб лишити тільки "видимі" символи
# chars_count = len(full_text.replace(" ", "").replace("\n", ""))

# # Формуємо словник для JSON
# result = {
#     "lines": lines_count,
#     "words": words_count,
#     "chars": chars_count
# }

# # 3. Зберігаємо результат у stats.json
# with open('stats.json', 'w', encoding='utf-8') as f:
#     json.dump(result, f, indent=4)

# print("Готово! Статистика збережена в stats.json")