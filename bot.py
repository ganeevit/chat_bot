import logging
import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

YANDEX_API_URL = "https://api.weather.yandex.ru/v2/forecast"
YANDEX_API_KEY = os.getenv("YANDEX_API_KEY", "YOUR_YANDEX_API_KEY")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")


logging.basicConfig(level=logging.INFO)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привет! Отправьте название города, и я пришлю прогноз погоды на неделю из Яндекс Погоды."
    )


def get_weather(city: str) -> str:
    params = {
        "geocode": city,
        "lang": "ru_RU",
        "limit": 7,
        "hours": False,
        "extra": False,
    }
    headers = {"X-Yandex-API-Key": YANDEX_API_KEY}
    try:
        response = requests.get(YANDEX_API_URL, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        logging.error("Failed to fetch weather: %s", e)
        return "Не удалось получить данные о погоде."

    if "forecasts" not in data:
        return "Не удалось получить данные о погоде."

    result_lines = [f"Прогноз погоды для {city}:"]
    for day in data["forecasts"]:
        date = day.get("date")
        day_part = day.get("parts", {}).get("day", {})
        condition = day_part.get("condition")
        temp_min = day_part.get("temp_min")
        temp_max = day_part.get("temp_max")
        result_lines.append(f"{date}: {condition}, от {temp_min} до {temp_max} °C")
    return "\n".join(result_lines)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    city = update.message.text
    weather = get_weather(city)
    await update.message.reply_text(weather)


def main() -> None:
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()


if __name__ == "__main__":
    main()
