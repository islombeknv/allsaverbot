from datetime import datetime
from typing import Tuple, Any

import pytz
from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from data.config import ADMINS
from keyboards.inline.lang import lang
from app import I18N_DOMAIN, LOCALES_DIR
from loader import dp
from save import save_user
from states.adnsstate import myadminstate

LANG_STORAGE = {}
LANGS = ["en", "uz", 'ru']


class Localization(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:
        user: types.User = types.User.get_current()

        if LANG_STORAGE.get(user.id) is None:
            LANG_STORAGE[user.id] = "en"
        *_, data = args
        language = data['locale'] = LANG_STORAGE[user.id]
        return language


i18n = Localization(I18N_DOMAIN, LOCALES_DIR)
dp.middleware.setup(i18n)
_ = i18n.gettext


@dp.message_handler(commands='start', state=myadminstate)
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(_(f"🔥 Welcome, You can download via bot:\n\n"
                           f"• Instagram - stories, highlights, post and IGTV;\n"
                           f"• YouTube - video/audio in any format!;\n"
                           f"• TikTok - video without watermark;\n"
                           f"• Likee - video without watermark;\n"
                           f"• Pinterest - photo, video and gif;\n"
                           f"• Facebook - video;\n"
                           f"• Twitter - photo and video.\n\n"
                           f"🚀 Send its link to start downloading media.\n"
                           f"🌐 Change bot language\n"),
                         reply_markup=lang())


@dp.message_handler(commands=['start', 'lang'])
async def bot_start(message: types.Message):
    await message.answer(_(f"🔥 Welcome, You can download via bot:\n\n"
                           f"• Instagram - stories, highlights, post and IGTV;\n"
                           f"• YouTube - video/audio in any format!;\n"
                           f"• TikTok - video without watermark;\n"
                           f"• Likee - video without watermark;\n"
                           f"• Pinterest - photo, video and gif;\n"
                           f"• Facebook - video;\n"
                           f"• Twitter - photo and video.\n\n"
                           f"🚀 Send its link to start downloading media.\n"
                           f"🌐 Change bot language\n"),
                         reply_markup=lang())


@dp.callback_query_handler(text=['uz', 'ru', 'en'])
async def myorder(call: CallbackQuery):
    await dp.bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'uz':
        LANG_STORAGE[call.from_user.id] = 'uz'
        await call.message.answer("Media yuklashni boshlash uchun uning havolasini yuboring.",
                                  reply_markup=ReplyKeyboardRemove())
    elif call.data == 'en':
        LANG_STORAGE[call.from_user.id] = 'en'
        await call.message.answer("Send its link to start downloading media.",
                                  reply_markup=ReplyKeyboardRemove())
    elif call.data == 'ru':
        LANG_STORAGE[call.from_user.id] = 'ru'
        await call.message.answer(" Отправьте ссылку, чтобы начать загрузку медиа.",
                                  reply_markup=ReplyKeyboardRemove())

    if save_user(call.message, call.data) == 201:

        join = datetime.now(pytz.timezone('Asia/Tashkent')).strftime('%Y-%m-%d, %H:%M')

        for admin in ADMINS:
            txt = f"Yangi foydalanuvchi qo'shildi:\n" \
                  f"<b>Vaqti:</b> {join}\n" \
                  f"<b>Tili:</b> {call.data}\n" \
                  f"<b>User:</b> <a href='tg://user?id={call.message.chat.id}'>" \
                  f"{call.message.chat.first_name}</a>"

            await dp.bot.send_message(admin, txt, parse_mode='HTML')
