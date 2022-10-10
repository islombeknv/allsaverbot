from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

adnsbtn1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='❌ Bekor qilish'),
        ],
    ],
    resize_keyboard=True
)

adnsbtn2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅ Tasdiqlash'),
            KeyboardButton(text='❌ Bekor qilish'),
        ],
    ],
    resize_keyboard=True
)