from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ReplyKeyboardRemove

from button import menu_button, python_button, start_button

# from config import dp


BOT_TOKEN = '6538736550:AAGUxaYjBWdwbERkVkyYA9FbaxjcD-oMVSc'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_fun(msg: Message):
    text = f"Assalomu alaykum {msg.from_user.full_name} 🤖Botimizga Xush kelibsiz!!!"
    await msg.answer(text, reply_markup=start_button)


@dp.message_handler(commands=['help'])
async def start_fun(msg: Message):
    text = f"Yordam kerak bo'lsa quyidagi nomerga murojat qiling.\n 📞️ +998 91 234 56 78"
    await msg.answer(text)


@dp.message_handler(text="Menu📲️")
async def menu_fun(msg: Message):
    text = "Yo'nalishlardan birini tanlang: "
    await msg.answer(text, reply_markup=menu_button)


@dp.message_handler(text="Orqaga👉")
async def orqaga_fun(msg: Message):
    text = "Bita chiqish: "
    await msg.answer(text, reply_markup=menu_button)


@dp.message_handler(text="Python🐍")
async def python_fun(msg: Message):
    text = "Darslardan birini tanlang: "
    await msg.answer(text, reply_markup=python_button)


@dp.message_handler(text="#001-dars")
async def dars1_fun(msg: Message):
    await msg.answer('https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=2268s')


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)