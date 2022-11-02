from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove,InputFile,ContentType
import random
import sqlite3

from Mysecrets.Mysecrets import Bot_token
from parsing.parsing import parser

parser()

bot = Bot(token=Bot_token)
dp = Dispatcher(bot)

db = sqlite3.connect('jokes.db')
cur = db.cursor()

async def on_startup(_):
   print("Бот запущен")

b1 = KeyboardButton("🌚 Чёрные шутки 🌚")
b2 = KeyboardButton("🔥 Мемы в картинках 🔥")
b3 = KeyboardButton("👎 Шутки про штирлица 🤷‍♂️")
b4 = KeyboardButton("🤩 Добавить свою шутку 🤩")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(b1,b2,b3).add(b4)

@dp.message_handler(commands=["start","help"])
async def command_start(message : types.Message):
   await message.answer(" 😝 Здарова холоп 😝 ")
   await message.answer(" 🤡 Выбери категорию 🤡 ",reply_markup=kb_client)

@dp.message_handler(text=["🌚 Чёрные шутки 🌚"])
async def black_jokes(message : types.Message):
   cur.execute(f'''
   SELECT black_joke FROM black_jokes ORDER BY RANDOM() LIMIT 1;''')
   record = cur.fetchone()
   await message.answer(record[0])

@dp.message_handler(text=["🔥 Мемы в картинках 🔥"])
async def Memes_pic(message : types.Message):
   cur.execute(f'''
   SELECT Meme_pic FROM Memes_pic ORDER BY RANDOM() LIMIT 1;''')
   record = cur.fetchone()
   await bot.send_photo(chat_id=message.chat.id, photo=record[0])

@dp.message_handler(text=["👎 Шутки про штирлица 🤷‍♂️"])
async def stirlitz(message : types.Message):
   cur.execute(f'''
   SELECT stirlitz_joke FROM stirlitz ORDER BY RANDOM() LIMIT 1;''')
   record = cur.fetchone()
   await message.answer(record[0])

@dp.message_handler(text=["🤩 Добавить свою шутку 🤩"])
async def add_joke(message : types.Message):
   await message.answer("Напиши свою шутку:")

@dp.message_handler(content_types=ContentType.PHOTO)
async def send_foto(message : types.Message):
   await message.answer(message.photo[-1].file_id)

@dp.message_handler()
async def jokes(message : types.Message):
      await message.answer("😡 Нет такой команды. Напиши /start")

executor.start_polling(dp, skip_updates=True,on_startup=on_startup)