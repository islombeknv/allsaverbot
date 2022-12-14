import requests
from aiogram import types
from loader import dp


@dp.message_handler(commands='report')
async def bot_help(message: types.Message):
    data = requests.get(f'http://127.0.0.1:8000/users/').json()
    text = (f"πΉ<b> Bot statistikasi</b>\n\n"
            f"π₯<b> Foydalanuvchilar soni</b>\n\n"
            f"π Umumiy - <code>{data['total']}</code> kishi\n",
            f"πΉ Bugun - <code>{data['day']}</code> kishi",
            f"πΉ Oy - <code>{data['month']}</code> kishi",
            f"πΉ yil - <code>{data['year']}</code> kishi\n",
            f"<b>Foydalanuvchilar til</b>\n",
            f"πΊπΏ Uzbek - <code>{data['uzb']}</code> kishi",
            f"πΊπΈ English - <code>{data['eng']}</code> kishi",
            f"π·πΊ Russia - <code>{data['rus']}</code> kishi\n",
            f"@Alpha4Groupbot",
            )
    await message.answer("\n".join(text), parse_mode='HTML')
