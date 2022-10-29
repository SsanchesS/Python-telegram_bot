from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
token='5685200265:AAHOtaQklpX7O3Ghx89jswFVbjvO0VWtLo4'

bot = Bot(token=token)
dp = Dispatcher(bot)

async def on_startup(_):
   print("Бот запущен")

# Клиентская часть

b1 = KeyboardButton("Чёрные_шутки")
b2 = KeyboardButton("Мемы_в_картинках")
b3 = KeyboardButton("3_категория")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(b1,b2,b3)

@dp.message_handler(commands=["start","help"])
async def command_start(message : types.Message):
      await message.answer("Выбери категорию: ",reply_markup=kb_client)

@dp.message_handler(text=["Чёрные_шутки", "Мемы_в_картинках", "3_категория"])
async def jokes(message : types.Message):
      await message.answer(message.text)

@dp.message_handler()
async def jokes(message : types.Message):
      await message.answer("Нет такой команды. Напиши /start ")

# Админская часть


# Общая часть


executor.start_polling(dp, skip_updates=True,on_startup=on_startup)













