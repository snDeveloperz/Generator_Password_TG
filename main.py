import random
import string
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv
import os


# Загружаем токен бота из файла .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Функция генерации сложного пароля
def generate_strong_password(length: int) -> str:
    if length < 6 or length > 50:
        return None  # Ограничение на длину
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))



# Функция генерации запоминающегося пароля
def generate_memorable_password(words_count: int) -> str:
    word_list = [
    "aurora", "breeze", "crystal", "dolphin", "emerald", "firefly", "glacier", "harmony", "illusion", "journey",
    "karma", "lighthouse", "moonlight", "nebula", "oasis", "paradox", "quicksilver", "rhapsody", "serenity", "twilight",
    "utopia", "voyager", "whisper", "xylophone", "yonder", "zenith", "atlas", "blossom", "cascade", "daybreak",
    "echo", "fable", "gravity", "horizon", "infinity", "jasmine", "kaleidoscope", "labyrinth", "mirage", "nirvana",
    "oracle", "pinnacle", "quasar", "radiance", "solstice", "tundra", "universe", "vortex", "wonderland", "zephyr","apple", "banana", 
    "cherry", "delta", "eagle", "falcon", "giraffe", "horizon", "island", "jungle", "kiwi", "lemon", "mango", "nectar", "ocean", "panda", 
    "quantum", "rocket", "sunset", "tiger", "universe", "volcano", "winter","xenon", "yellow", "zebra", "alpha", "bravo", 
    "comet","dragon", "ember", "forest", "galaxy", "horizon", "iceberg", "jupiter", "kangaroo", "lantern", 
    "meteor", "nebula", "orion", "phoenix", "quasar", "rainbow", "starlight", "tornado", "utopia", "vortex", "wildfire", "zephyr"]
    if words_count < 2 or words_count > 5:
        return None  
    return '-'.join(random.sample(word_list, words_count))


# Обработчик команды /start
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Я бот для генерации паролей.\nВыбери команду:\n/password [длина] - Сложный пароль\n/memopass [кол-во слов] - Запоминающийся пароль")

# Обработчик команды /password для генерации сложного пароля
@dp.message(Command("password"))
async def password_handler(message: Message):
    args = message.text.split()
    if len(args) < 2 or not args[1].isdigit():
        await message.answer("Ошибка! Укажите длину пароля, например: /password 12")
        return
    
    length = int(args[1])
    password = generate_strong_password(length)
    if password is None:
        await message.answer("Ошибка! Длина пароля должна быть от 6 до 50 символов.")
    else:
        await message.answer(f"Ваш пароль: `{password}`", parse_mode="Markdown")

# Обработчик команды /memopass для генерации запоминающегося пароля
@dp.message(Command("memopass"))
async def memopass_handler(message: Message):
    args = message.text.split()
    if len(args) < 2 or not args[1].isdigit():
        await message.answer("Ошибка! Укажите количество слов, например: /memopass 3")
        return
    
    words_count = int(args[1])
    password = generate_memorable_password(words_count)
    if password is None:
        await message.answer("Ошибка! Количество слов должно быть от 2 до 5.")
    else:
        await message.answer(f"Ваш запоминающийся пароль:  `{password}`", parse_mode="Markdown")

# Запуск бота
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())