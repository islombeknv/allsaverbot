import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.adns import adnsbtn1, adnsbtn2
from keyboards.inline.adnsibtn import adnsbtn
from loader import dp
from states.adnsstate import myadminstate

SUPERUSERS = [354064378, 885947803]


@dp.message_handler(commands='adsense', chat_id=SUPERUSERS)
async def adsenses(message: types.Message):
    await message.answer('🔰 Botga reklama joylash 3 bosqichda:\n\n'
                         '1. Reklama qo\'shish\n'
                         '2. Link qo\'shish\n'
                         '3. Tasdiqlash\n\n'
                         'Davom etish uchun reklama materialini yuboring',
                         reply_markup=adnsbtn1)
    await myadminstate.first_step.set()


@dp.message_handler(content_types=['video', 'photo', 'text'], state=myadminstate.first_step)
async def adns1(message: types.Message, state: FSMContext):
    if message.text == '❌ Bekor qilish':
        await message.answer('🚫 Botga reklama joylash bekor qilindi',
                             reply_markup=ReplyKeyboardRemove())
        await state.finish()

    else:
        if message.content_type == 'photo':
            await state.update_data(
                {
                    "photo": message.photo[-1].file_id,
                    "caption": message.caption,
                }
            )

        elif message.content_type == 'video':
            await state.update_data(
                {
                    "video": message.video.file_id,
                    "caption": message.caption,
                }
            )
        elif message.text:
            await state.update_data({"text": message.text})

        await message.answer('🔗 Tugmali url uchun link yuboring\n\n'
                             'Yuborilishi: title + url \n'
                             'Namuna: <code>🌐 Sayt + kun.uz</code>\n\n'
                             'Agar sizga bu kerak bo\'lmasa, bosing👉 /next',
                             reply_markup=adnsbtn1, parse_mode='HTML')
        await myadminstate.second_step.set()


@dp.message_handler(state=myadminstate.second_step)
async def adns2(message: types.Message, state: FSMContext):
    if message.text == '❌ Bekor qilish':

        await message.answer('🚫 Botga reklama joylash bekor qilindi', reply_markup=ReplyKeyboardRemove())
        await state.finish()

    elif message.text != '❌ Bekor qilish':
        db = await state.get_data()

        try:
            if db.get('photo'):
                if message.text == '/next':
                    await message.answer_photo(db.get('photo'), db.get('caption'))
                else:
                    await message.answer_photo(db.get('photo'), db.get('caption'),
                                               reply_markup=adnsbtn(message.text))

            elif db.get('video'):

                if message.text == '/next':
                    await message.answer_video(db.get('video'), caption=db.get('caption'))
                else:
                    await message.answer_video(db.get('video'), caption=db.get('caption'),
                                               reply_markup=adnsbtn(message.text))
            elif db.get('text'):

                if message.text == '/next':
                    await message.answer(db.get("text"))
                else:
                    await message.answer(db.get("text"), reply_markup=adnsbtn(message.text))

            if message.text == '/next':
                await state.update_data(
                    {
                        "next": message.text,
                    }
                )
            else:
                await state.update_data(
                    {
                        "url": message.text,
                    }
                )

            await message.answer('Reklama tayyor endi, tasdiqlang', reply_markup=adnsbtn2)
            await myadminstate.third_step.set()

        except:
            await myadminstate.second_step.set()
            await message.answer('Xato malumot kiritildi, ehtimol '
                                 'kiritilgan url yaroqsizdir, qayta tekshirib yuboring', reply_markup=adnsbtn1)


@dp.message_handler(state=myadminstate.third_step)
async def adns3(message: types.Message, state: FSMContext):
    data = requests.get(f'http://127.0.0.1:8000/users/list/').json()
    if message.text == '❌ Bekor qilish':
        await message.answer('🚫 Botga reklama joylash bekor qilindi', reply_markup=ReplyKeyboardRemove())
        await state.finish()

    db = await state.get_data()

    try:
        if message.text == '✅ Tasdiqlash' and data:
            if db.get('photo'):
                if db.get('next'):
                    for i in data:
                        await dp.bot.send_photo(i['tg_id'], db.get('photo'), db.get('caption'))
                else:
                    for i in data:
                        await dp.bot.send_photo(i['tg_id'], db.get('photo'), db.get('caption'),
                                                reply_markup=adnsbtn(db.get('url')))

            elif db.get('video'):

                if db.get('next'):
                    for i in data:
                        await dp.bot.send_video(i['tg_id'], db.get('video'), caption=db.get('caption'))
                else:
                    for i in data:
                        await dp.bot.send_video(i['tg_id'], db.get('video'), caption=db.get('caption'),
                                                reply_markup=adnsbtn(db.get('url')))
            elif db.get('text'):

                if db.get('next'):
                    for i in data:
                        await dp.bot.send_message(i['tg_id'], db.get("text"))
                else:
                    for i in data:
                        await dp.bot.send_message(i['tg_id'], db.get("text"),
                                                  reply_markup=adnsbtn(db.get('url')))
            await state.finish()
            await message.answer('🎉 Reklama botga muvaffaqiyatli yuklandi', reply_markup=ReplyKeyboardRemove())

    except:
        await myadminstate.first_step.set()
        await message.answer('Xato malumot kiritildi, ehtimol '
                             'kiritilgan url yaroqsizdir, qayta tekshirib yuboring\n\n'
                             'Davom etish uchun reklama materialini yuboring', reply_markup=adnsbtn1)
