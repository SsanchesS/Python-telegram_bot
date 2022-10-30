from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
import random
import json

from Mysecrets import Bot_token
from parsing.parsing import parser

parser()

with open("jokes.json","r") as json_file:
      jokes_json = json.load(json_file)

bot = Bot(token=Bot_token)
dp = Dispatcher(bot)

async def on_startup(_):
   print("Бот запущен")

b1 = KeyboardButton("Чёрные_шутки")
b2 = KeyboardButton("Мемы_в_картинках")
b3 = KeyboardButton("Шутки_про_штирлица")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(b1,b2,b3)

@dp.message_handler(commands=["start","help"])
async def command_start(message : types.Message):
      await message.answer("Выбери категорию: ",reply_markup=kb_client)

@dp.message_handler(text=["Чёрные_шутки", "Мемы_в_картинках", "Шутки_про_штирлица"])
async def jokes(message : types.Message):
   if message.text == "Чёрные_шутки":
      await message.answer(random.choice(jokes_json['black_jokes']))
   elif message.text == "Мемы_в_картинках":
      await bot.send_photo(chat_id=message.chat.id, photo=random.choice(jokes_json['Memes_pic']))
   elif message.text == "Шутки_про_штирлица":
      await message.answer(random.choice(jokes_json['stirlitz']))

@dp.message_handler()
async def jokes(message : types.Message):
      await message.answer("Нет такой команды. Напиши /start ")

executor.start_polling(dp, skip_updates=True,on_startup=on_startup)