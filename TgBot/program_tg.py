import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.enums import ParseMode
import psycopg2
import os
import datetime

# Environment variables for API key and database URL
TELEGRAM_BOT_API_KEY = os.getenv('TOKENTG')
DATABASE_URL = os.getenv('DB_URL')

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=TELEGRAM_BOT_API_KEY, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Dictionary to store user feedback temporarily
user_feedback_data = {}


# User state constants
class UserState:
    WELCOME = 0
    FEEDBACK = 1
    PROJECTS = 2
    ONLINE_SOMMELIER = 3
    FEEDBACK_TEXT = 4
    FEEDBACK_ANON = 5


# Function to get a connection to the database
def get_database_connection():
    return psycopg2.connect(DATABASE_URL, sslmode='require')


# Handler for the /start command
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    feedback_button = KeyboardButton('Залишити відгук')
    projects_button = KeyboardButton('Проекти')
    markup.add(feedback_button, projects_button)
    await message.answer("Вітаю!\nЯ телеграм бот, проекту 'Онлайн Сомельє'\nБудь-ласка оберіть функцію.",
                         reply_markup=markup)
    user_feedback_data[message.from_user.id] = {'state': UserState.WELCOME}


# Handler for feedback button
@dp.message(lambda message: message.text == 'Залишити відгук')
async def leave_feedback(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    back_button = KeyboardButton('Назад')
    markup.add(back_button)
    await message.answer("Будь ласка, залиште ваш відгук.", reply_markup=markup)
    user_feedback_data[message.from_user.id]['state'] = UserState.FEEDBACK_TEXT


# Handler for projects button
@dp.message(lambda message: message.text == 'Проекти')
async def show_projects(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    project_online_sommilie_button = KeyboardButton('Онлайн Сомельє')
    back_button = KeyboardButton('Назад')
    markup.add(project_online_sommilie_button, back_button)
    await message.answer("Проекти", reply_markup=markup)
    user_feedback_data[message.from_user.id]['state'] = UserState.PROJECTS


# Handler for back button
@dp.message(lambda message: message.text == 'Назад')
async def go_back(message: types.Message):
    await send_welcome(message)


# Handler for handling feedback steps
@dp.message(lambda message: message.text not in ['Залишити відгук', 'Проекти', 'Назад'])
async def handle_feedback(message: types.Message):
    state = user_feedback_data.get(message.from_user.id, {}).get('state', UserState.WELCOME)

    if state == UserState.FEEDBACK_TEXT:
        user_feedback_data[message.chat.id] = {'feedback': message.text, 'time': datetime.datetime.now()}
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        anon_button = KeyboardButton('Залишити анонімно')
        tg_name_button = KeyboardButton('Залишити з ім\'ям Telegram')
        back_button = KeyboardButton('Назад')
        markup.add(anon_button, tg_name_button, back_button)
        await message.answer("Ви бажаєте залишити відгук анонімно чи з вашим ім'ям Telegram?", reply_markup=markup)
        user_feedback_data[message.from_user.id]['state'] = UserState.FEEDBACK_ANON

    elif state == UserState.FEEDBACK_ANON:
        if message.text == 'Залишити анонімно':
            user_feedback_data[message.chat.id]['name'] = 'анонім'
            await save_feedback(message.chat.id)
            await message.answer("Дякуємо за ваш відгук!")
            await send_welcome(message)
        elif message.text == 'Залишити з ім\'ям Telegram':
            user_feedback_data[message.chat.id]['name'] = message.from_user.first_name or 'анонім'
            await save_feedback(message.chat.id)
            await message.answer("Дякуємо за ваш відгук!")
            await send_welcome(message)

    elif state == UserState.PROJECTS:
        if message.text == 'Онлайн Сомельє':
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            git_hub_button = KeyboardButton('GitHub проекта')
            site_button = KeyboardButton('Посилання на проект')
            project_info_button = KeyboardButton('Про проект')
            back_button = KeyboardButton('Назад')
            markup.add(git_hub_button, site_button, project_info_button, back_button)
            await message.answer("Онлайн Сомельє", reply_markup=markup)
            user_feedback_data[message.from_user.id]['state'] = UserState.ONLINE_SOMMELIER

        elif message.text == 'Назад':
            await send_welcome(message)

    elif state == UserState.ONLINE_SOMMELIER:
        if message.text == 'GitHub проекта':
            await message.answer("https://github.com/Bevziuk2005/Sommelier_Online.git")
        elif message.text == 'Посилання на проект':
            await message.answer("https://sommelier-online.onrender.com")
        elif message.text == 'Про проект':
            await message.answer(
                "Сайт пропонує користувачам можливість отримати професійні рекомендації щодо вибору вин та їх поєднання з їжею. На сайті є:\n\n- база даних з найпопулярніших вин світу;\n- зручний інтерфейс;\n- реєстрація для зручного збереження обраних вин;\n- історична довідка про виготовлення та особливості вин;\n- пошук, який дозволяє швидко отримати інформацію про будь-яке вино;\n\nСайт орієнтований як на новачків, так і на досвідчених поціновувачів вина, надаючи зручний інтерфейс та корисні інструменти для вибору ідеального вина для будь-якої нагоди.")
        elif message.text == 'Назад':
            await show_projects(message)


# Function to save feedback to the database
async def save_feedback(chat_id):
    data = user_feedback_data.get(chat_id)
    if data:
        try:
            with get_database_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("INSERT INTO feedback (name, feedback, time) VALUES (%s, %s, %s)",
                                   (data['name'], data['feedback'], data['time']))
                    conn.commit()
        except Exception as e:
            logger.error(f"Error saving feedback: {e}")
        finally:
            del user_feedback_data[chat_id]


# Start the bot
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
