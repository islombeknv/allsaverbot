from aiogram import types


def tiktokbtn():
    btn = types.InlineKeyboardMarkup(one_time_keyboard=True)
    btn.add(types.InlineKeyboardButton('🎧 MP3', callback_data='ttmp3'),
            types.InlineKeyboardButton('SHARE ⬏', switch_inline_query='tiktok'))

    return btn


def instabtn():
    btn = types.InlineKeyboardMarkup(one_time_keyboard=True)
    btn.add(types.InlineKeyboardButton('SHARE ⬏', switch_inline_query='tiktok'))

    return btn
