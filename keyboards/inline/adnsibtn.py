from aiogram import types


def adnsbtn(data):
    btn = types.InlineKeyboardMarkup(row_width=3)
    btn.insert((types.InlineKeyboardButton(data.split('+ ')[0], url=data.split('+ ')[1])))
    return btn
