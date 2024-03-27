from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Menu📲️")
        ]
    ],
    resize_keyboard=True
)

menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Python🐍"),
            KeyboardButton("Foundation🤖"),
            KeyboardButton("Django💻")

        ],
        [
            KeyboardButton("Menu📲️")
        ]
    ],
    resize_keyboard=True
)

python_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("#001-dars"),
            KeyboardButton("#002-dars"),
            KeyboardButton("#003-dars"),
            KeyboardButton("#004-dars")
        ],
        [
            KeyboardButton("#005-dars"),
            KeyboardButton("#006-dars"),
            KeyboardButton("#007-dars"),
            KeyboardButton("#008-dars")
        ],
        [
            KeyboardButton("Orqaga👉"),
            KeyboardButton("Menu📲️")
        ]
    ],
    resize_keyboard=True
)