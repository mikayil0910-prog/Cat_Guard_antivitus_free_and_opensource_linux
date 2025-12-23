import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import logging

# Включим логирование для отладки
logging.basicConfig(level=logging.INFO)

TELEGRAM_TOKEN = "8343097394:AAE527lxFv-8vdfjP54c1Y50Z5lIIs9XokA"
OPENROUTER_API_KEY = "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"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот с интеграцией DeepSeek. Задайте мне вопрос!")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text

    # Добавим индикатор набора сообщения
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

    response = query_deepseek_openrouter(user_input)
    await update.message.reply_text(response)


def query_deepseek_openrouter(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://t.me/",
        "X-Title": "Telegram DeepSeek Bot"
    }
    data = {
        "model": "deepseek/deepseek-chat",  # Исправлено: правильный формат модели
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 1000,
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        logging.info(f"OpenRouter Status Code: {response.status_code}")

        if response.status_code != 200:
            logging.error(f"OpenRouter Error: {response.text}")
            return f"Ошибка API: {response.status_code}. Подробности в логах."

        result = response.json()
        return result["choices"][0]["message"]["content"]

    except requests.exceptions.RequestException as e:
        logging.error(f"Request error: {e}")
        return "Ошибка соединения с API. Попробуйте позже."
    except KeyError as e:
        logging.error(f"Key error in response: {e}, Response: {result if 'result' in locals() else 'No result'}")
        return "Ошибка обработки ответа от API."
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return "Произошла непредвиденная ошибка."


def main():
    try:
        app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

        print("Бот запущен...")
        app.run_polling()

    except Exception as e:
        print(f"Ошибка при запуске бота: {e}")


if __name__ == "__main__":
    main()