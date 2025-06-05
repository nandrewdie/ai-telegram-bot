import os
import asyncio
import requests
import json
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Загружаем переменные окружения
load_dotenv()

# Инициализация бота
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()

# Параметры YandexGPT
YANDEX_API_KEY = os.getenv('YANDEX_API_KEY')
YANDEX_FOLDER_ID = os.getenv('YANDEX_FOLDER_ID')


def get_yandex_response(user_text):
    """Получение ответа от YandexGPT"""
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {YANDEX_API_KEY}"
    }

    data = {
        "modelUri": f"gpt://{YANDEX_FOLDER_ID}/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.7,
            "maxTokens": 1000
        },
        "messages": [
            {
                "role": "system",
                "text": "Ты дружелюбный помощник. Отвечай на русском языке."
            },
            {
                "role": "user",
                "text": user_text
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        return result['result']['alternatives'][0]['message']['text']
    else:
        return f"Ошибка API: {response.status_code} - {response.text}"


@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(
        "Привет! 👋 Я бот на базе YandexGPT.\n"
        "Задавай любые вопросы!"
    )


@dp.message()
async def handle_message(message: types.Message):
    try:
        # Показываем, что бот печатает
        await bot.send_chat_action(
            chat_id=message.chat.id,
            action="typing"
        )

        # Получаем ответ от YandexGPT
        response = get_yandex_response(message.text)

        # Отправляем ответ
        await message.answer(response)

    except Exception as e:
        await message.answer(f"Произошла ошибка: {str(e)}")


async def main():
    print("Бот запущен с YandexGPT!")
    print(f"Folder ID: {YANDEX_FOLDER_ID}")
    print(f"API Key: {YANDEX_API_KEY[:10]}...")
    if not YANDEX_API_KEY or not YANDEX_FOLDER_ID:
        print("ОШИБКА: Не заданы YANDEX_API_KEY или YANDEX_FOLDER_ID!")
        return  # ← только если есть ошибка, выходим
    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        print("Работа бота остановлена пользователем")
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Программа завершена вручную")