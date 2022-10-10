from aiogram import types


def youtubebtn():
    btn = types.InlineKeyboardMarkup(row_width=3)
    btn.insert(types.InlineKeyboardButton('📹 720', callback_data='yt,720'))
    btn.insert(types.InlineKeyboardButton('📹 360', callback_data='yt,360'))
    btn.insert(types.InlineKeyboardButton('📹 144', callback_data='yt,144'))
    btn.insert(types.InlineKeyboardButton('🎧 MP3', callback_data='ytmp3'))
    return btn
