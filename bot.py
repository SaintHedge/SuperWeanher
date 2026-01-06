from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт! 🌤\nНапиши /weather — покажу погоду в Кременчуку"
    )

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        "?q=Kremenchuk&units=metric&lang=uk"
        f"&appid={WEATHER_API_KEY}"
    )
    data = requests.get(url).json()

    await update.message.reply_text(
        f"🌡 Температура: {data['main']['temp']}°C\n"
        f"☁️ Опис: {data['weather'][0]['description']}"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("weather", weather))

    app.run_polling()

if __name__ == "__main__":
    main()
