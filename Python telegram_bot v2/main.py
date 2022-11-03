from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher,FSMContext
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove,ContentType
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import sqlite3

from Mysecrets.Mysecrets import Bot_token, Admin
from parsing.parsing import parser

parser()

class FSMAdd_joke(StatesGroup):
   user_joke = State()

# class FSMAdmin(StatesGroup):
#    check_user_jokes = State()

bot = Bot(token=Bot_token)
dp = Dispatcher(bot,storage=MemoryStorage())

db = sqlite3.connect('jokes.db')
cur = db.cursor()

async def on_startup(_):
   print("Бот запущен")

b1 = KeyboardButton("🌚 Чёрные шутки 🌚")
b2 = KeyboardButton("🔥 Мемы в картинках 🔥")
b3 = KeyboardButton("✊ Шутки про штирлица 👊")
b4 = KeyboardButton("🤩 Добавить свою шутку 🤩")
b5 = KeyboardButton("😎 Шутки пользователей 😎") 

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(b1,b2,b3).add(b5).add(b4)

@dp.message_handler(commands=["start","help"])
async def command_start(message : types.Message):
   await message.answer("😝 Здарова холоп 😝")
   await message.answer("🤡 Выбери категорию 🤡",reply_markup=kb_client)

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

@dp.message_handler(text=["✊ Шутки про штирлица 👊"])
async def stirlitz(message : types.Message):
   cur.execute(f'''
   SELECT stirlitz_joke FROM stirlitz ORDER BY RANDOM() LIMIT 1;''')
   record = cur.fetchone()
   await message.answer(record[0])

@dp.message_handler(text=["😎 Шутки пользователей 😎"])
async def users_jokes(message : types.Message):
   cur.execute(f'''
   SELECT joke FROM users_jokes ORDER BY RANDOM() LIMIT 1;''')
   record = cur.fetchone()
   if record:
      await message.answer(record[0])
   else:
      await message.answer("Список шуток пуст :(")

# 
# @dp.message_handler(commands=["admin"])
# async def command_admin(message : types.Message):
#    if message.chat.id == Admin:
#       print("🦄 Зашёл Создатель 🦄")
#       await message.answer("💪 Здаравия желаю, мой господин 🤝",reply_markup=ReplyKeyboardRemove())
#       await message.answer("Для модерации шуток пользователей напиши: /viewing_user_jokes")
#       await message.answer("Для того, чтобы узнать id фото: отправь мне фото")
#    else:
#       await message.answer("🖕 Катись отседава 🖕")

# @dp.message_handler(commands=["viewing_user_jokes"])
# async def viewing_user_jokes(message : types.Message):
#    cur.execute(f'''
#    SELECT joke FROM users_jokes ORDER BY RANDOM() LIMIT 1;''')
#    record = cur.fetchone()
#    await message.answer(record[0])

# 
@dp.message_handler(text=["🤩 Добавить свою шутку 🤩"])
async def Fsm_AddUserJoke_start(message : types.Message):
   await FSMAdd_joke.user_joke.set()
   await message.answer("Напиши свою шутку:",reply_markup=ReplyKeyboardRemove())
   await message.answer("* Ты можешь написать только текстовую шутку *")

async def add_user_joke(state):
   async with state.proxy() as data:
      cur.executescript(f'''
         INSERT INTO users_jokes (joke,author_joke) VALUES ('{data["text"]}','{data["chat_id"]}');''')
      db.commit() 

@dp.message_handler(state=FSMAdd_joke.user_joke)
async def add_joke(message : types.Message, state:FSMContext):
   async with state.proxy() as data:
      data["text"] = message.text
      data["chat_id"] = message.chat.id
   await add_user_joke(state)
   await message.answer("🧠 Шутка успешно добавлена 🏆")
   await state.finish()

# 
@dp.message_handler(content_types=ContentType.PHOTO)
async def send_foto(message : types.Message):
   await message.answer(message.photo[-1].file_id)

@dp.message_handler()
async def jokes(message : types.Message):
      await message.answer("😡 Нет такой команды. Напиши /start")

executor.start_polling(dp, skip_updates=True,on_startup=on_startup)
