from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove,InputFile
import random
import json

from Mysecrets.Mysecrets import Bot_token
from parsing.parsing import parser

parser()

with open("jokes.json","r") as json_file:
      jokes_json = json.load(json_file)

bot = Bot(token=Bot_token)
dp = Dispatcher(bot)

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
   await message.answer(random.choice(jokes_json['black_jokes']))

@dp.message_handler(text=["🔥 Мемы в картинках 🔥"])
async def Memes_pic(message : types.Message):
   await bot.send_photo(chat_id=message.chat.id, photo=InputFile(path_or_bytesio=random.choice(jokes_json['Memes_pic'])))

@dp.message_handler(text=["👎 Шутки про штирлица 🤷‍♂️"])
async def stirlitz(message : types.Message):
   await message.answer(random.choice(jokes_json['stirlitz']))

@dp.message_handler(text=["🤩 Добавить свою шутку 🤩"])
async def add_joke(message : types.Message):
   await message.answer("Напиши свою шутку:")

@dp.message_handler()
async def jokes(message : types.Message):
      await message.answer("😡 Нет такой команды. Напиши /start")

executor.start_polling(dp, skip_updates=True,on_startup=on_startup)