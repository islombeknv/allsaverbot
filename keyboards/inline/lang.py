from aiogram import types


def lang():
    btn = types.InlineKeyboardMarkup(row_width=3)
    btn.insert(types.InlineKeyboardButton('🇺🇿 UZB', callback_data='uz'))
    btn.insert(types.InlineKeyboardButton('🇷🇺 RUS', callback_data='ru'))
    btn.insert(types.InlineKeyboardButton('🇺🇸 ENG', callback_data='en'))
    return btn