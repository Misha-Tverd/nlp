import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import parse_text



load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")


CATEGORIES = {"food": []}


def detect_type(text):
    INCOME_KEYWORDS = ["зарплата", "дохід", "отримав", "отримала", "премія"]
    print(text)
    text = text.lower()
    if any(word in text for word in INCOME_KEYWORDS):
        return "income"
    return "expense"

def save_record(data, text, amount, type):
    os.path.exists("/data/records.csv")
    
    

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    amount = parse_text.parse_amount(text)
    if amount is None or amount == []:
        response = "Не вказана сума. Будь-ласка вкажіть суму"
    else:
        response = f"Витраченна сума: {amount}"
    await update.message.reply_text(response)
    await update.message.reply_text(detect_type(text))


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    print("Файл запущено")


    app.add_handler(MessageHandler(filters.ALL, handle_message))

    print("Application створено")

    app.run_polling()
    print("Після polling")



if __name__ == "__main__":
    main()
