import requests
from aiogram import types
from loader import dp


@dp.message_handler(commands='report')
async def bot_help(message: types.Message):
    data = requests.get(f'http://127.0.0.1:8000/users/').json()
    text = (f"💹<b> Bot statistikasi</b>\n\n"
            f"👥<b> Foydalanuvchilar soni</b>\n\n"
            f"🚀 Umumiy - <code>{data['total']}</code> kishi\n",
            f"🔹 Bugun - <code>{data['day']}</code> kishi",
            f"🔹 Oy - <code>{data['month']}</code> kishi",
            f"🔹 yil - <code>{data['year']}</code> kishi\n",
            f"<b>Foydalanuvchilar til</b>\n",
            f"🇺🇿 Uzbek - <code>{data['uzb']}</code> kishi",
            f"🇺🇸 English - <code>{data['eng']}</code> kishi",
            f"🇷🇺 Russia - <code>{data['rus']}</code> kishi\n",
            f"@Alpha4Groupbot",
            )
    await message.answer("\n".join(text), parse_mode='HTML')
