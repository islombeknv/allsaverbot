from aiogram import types


def lang():
    btn = types.InlineKeyboardMarkup(row_width=3)
    btn.insert(types.InlineKeyboardButton('πΊπΏ UZB', callback_data='uz'))
    btn.insert(types.InlineKeyboardButton('π·πΊ RUS', callback_data='ru'))
    btn.insert(types.InlineKeyboardButton('πΊπΈ ENG', callback_data='en'))
    return btn