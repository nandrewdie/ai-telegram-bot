AI Telegram Bot

Умный Telegram бот с использованием YandexGPT.

Возможности
-  Ведение диалогов с ИИ
-  Использование YandexGPT
-  Сохранение контекста беседы
-  Быстрые ответы

Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/nandrewdie/ai-telegram-bot.git
cd ai-telegram-bot
```
2. Создайте виртуальное окружение:
python -m venv venv
venv\Scripts\activate
3. Установите зависимости: 
pip install -r requirements.txt
4. Создайте файл .env и добавьте:
BOT_TOKEN=ваш_токен_от_BotFather
YANDEX_API_KEY=ваш_api_ключ
YANDEX_FOLDER_ID=ваш_folder_id
5. Запустите бота:
python bot.py

Технологии

Python 3.10+
aiogram 3.3.0
YandexGPT API
python-dotenv

Автор
nandrewdie
