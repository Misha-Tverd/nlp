# def parse_amount(text: str) -> list:
#     list_words = []
#     list_numbers = []
#     for word in text.split():
#         word = word.replace(',', '').replace('.', '')
#         if word.isdigit():
#             list_numbers.append(word)  
        
#     return list_numbers

# def detect_type(text):
#     INCOME_KEYWORDS = ["зарплата", "дохід", "отримав", "отримала", "премія"]
#     text = text.lower()
#     if any(word in text for word in INCOME_KEYWORDS):
#         return "income"
#     return "expense"
#     # # text = text.lower()
#     # print(type(text))
#     # if text in INCOME_KEYWORDS:
#     #     return "income"
#     # else:
#     #     return "expense"
    
# print(detect_type("Зарплата 120"))

from pathlib import Path
import csv
import datetime
import os


file_path = Path(__file__).parent / "records.csv"
print(file_path)
# data, text, amount, type
def save_record():
    print(file_path)
    if file_path:
        with open(file_path, mode="a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["amount", "desc"])
            print(writer)
            # for row in file:
            #     print(f"Дата: {row['data']}, text: {row['text']}")
            #     print("hello")
            # if len(file) == 0:
            #     print("hello")
    # print(file_path
    # if 
  
save_record()
  
from pathlib import Path
import csv

# 1. Визначаємо шлях правильно
current_dir = Path(__file__).parent
data_dir = current_dir / "data"
file_path = data_dir / "records.csv"

def save_record():
    # 2. Створюємо папку "data", якщо її немає (parents=True дозволяє створювати вкладені папки)
    data_dir.mkdir(parents=True, exist_ok=True)
    
    # 3. Перевіряємо, чи файл вже існує (для заголовків)
    file_exists = file_path.exists()
    
    print(f"Записую у файл: {file_path}")
    
    # 4. ВІДКРИВАЄМО БЕЗ ЛАПОК
    with open(file_path, mode="a", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        
        # Додаємо заголовок, якщо файл новий
        if not file_exists:
            writer.writerow(["date", "text", "amount", "type"])
            
        writer.writerow(["2024-05-15", "Продукти", "500", "expense"])
    
    print("Дані успішно збережено!")

save_record() 
  
  
  
  
  
  
    
# import csv

# def read_data():
#     with open('records.csv', mode='r', encoding='utf-8') as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             # Звертаємося до даних за назвою колонки
#             print(f"data: {row['data']}, text: {row['text']}")

# read_data()