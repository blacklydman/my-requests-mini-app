from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import json

TOKEN = "7005657844:AAFZUVhAk0xQRiNaQHNVvRUejCDi1zehDwk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
    [InlineKeyboardButton("Оставить заявку", web_app=WebAppInfo(url="https://Blacklydman.github.io/My-Requests-Mini-App/"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Нажми на кнопку, чтобы оставить заявку.", reply_markup=reply_markup)

async def handle_web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = json.loads(update.message.web_app_data.data)
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")
    reply = f"📥 Новая заявка:\n👤 {name}\n📧 {email}\n📝 {message}"
    await update.message.reply_text("Спасибо! Ваша заявка получена.")
    print(reply)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_web_app_data))
    print("Бот запущен!")
    app.run_polling()
