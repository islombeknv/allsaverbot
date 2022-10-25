import os

import requests
from aiogram import types
from aiogram.types import CallbackQuery

from dawnload import dowload_video, dowload_audio, likedownload, pinterest
from keyboards.inline.tiktok import tiktokbtn
from keyboards.inline.youtube import youtubebtn
from loader import dp, bot


@dp.message_handler()
async def bot_echo(message: types.Message):
    global mp3, caption, data
    try:
        if not message.text.startswith('https://likee.video/') | message.text.startswith('https://in.pinterest.com/'):
            data = requests.get(f'https://alirabie.host/APIs/D.php?url={message.text}').json()

        # pinterest
        if message.text.startswith('https://in.pinterest.com/'):
            await bot.send_chat_action(message.chat.id, 'upload_document')
            pint = pinterest(message.text)
            await message.answer_video(pint['data']['url'],
                                       caption=f"{pint['data']['title']}\n@Alpha4Groupbot")

        # likee
        elif message.text.startswith('https://likee.video/'):
            await bot.send_chat_action(message.chat.id, 'upload_document')
            video = likedownload(message.text)
            await message.answer_video(video,
                                       caption=f"@Alpha4Groupbot")

        # twitter
        elif data['hosting'] == 'twitter.com':
            await bot.send_chat_action(message.chat.id, 'upload_document')
            await message.answer_video(data['url'][0]['url'], caption='@Alpha4Groupbot')

        # facebook
        elif data['hosting'] == 'facebook.com':
            await bot.send_chat_action(message.chat.id, 'upload_document')
            await message.answer_video(data['url'][0]['url'], caption='@Alpha4Groupbot')

        # youtube start
        elif data['hosting'] == '101':
            text = f"📹 {data['meta']['title']}\n\n"
            await bot.send_chat_action(message.chat.id, 'upload_document')
            await message.answer_photo(data['thumb'], text, reply_markup=youtubebtn())

        # instagram start
        elif data['hosting'] == 'instagram.com':

            if data:
                # response = requests.get(data['url'][0]['url'])
                # open("instagram.mp4", "wb").write(response.content)
                # media = open(f'instagram.mp4', 'rb')
                await bot.send_chat_action(message.chat.id, 'upload_document')
                await message.answer_video(f"{data['url'][0]['url']}",
                                           caption=f"{data['meta']['title']}\n\n@Alpha4Groupbot")
                # media.close()
                #
                # if os.path.exists(f"instagram.mp4"):
                #     os.remove(f"instagram.mp4")

            elif message.text.split('/')[3] == 'stories':
                await bot.send_chat_action(message.chat.id, 'upload_document')
                await message.answer_video(data['url'][1]['url'],
                                           caption=f"{data['meta']['title']}\n\n@Alpha4Groupbot")


        # tiktok start
        elif data['hosting'] == 'tiktok.com':

            text = f"📹 {data['meta']['title']}\n⏱ {data['meta']['duration']}\n\n Format ↓  @Alpha4Groupbot"
            mp3 = f"{data['url'][1]['url']}"

            await bot.send_chat_action(message.chat.id, 'upload_document')

            await bot.delete_message(message.chat.id, message.message_id + 1)

            await message.answer_video(data['url'][0]['url'], caption=f'{text}',
                                       reply_markup=tiktokbtn())

    except:
        await message.answer("Invalid url😔")


@dp.callback_query_handler(text='ttmp3')
async def ttmp3(call: CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    await bot.send_chat_action(call.message.chat.id, 'upload_document')
    await call.message.answer_audio(mp3, caption='@Alpha4Groupbot')


@dp.callback_query_handler(text_startswith='yt,')
async def Admincall(call: CallbackQuery):
    ql = call.data.split(',')[1]

    if ql == '144':
        title = dowload_video(data['meta']['source'], 17)
    elif ql == '360':
        title = dowload_video(data['meta']['source'], 18)
    elif ql == '720':
        title = dowload_video(data['meta']['source'], 22)

    media = open(f'media/{title}', 'rb')

    await bot.send_chat_action(call.message.chat.id, 'upload_document')

    await bot.delete_message(call.message.chat.id, call.message.message_id)
    await call.message.answer_video(media,
                                    caption=f"📹 {data['meta']['title']}\n@Alpha4Groupbot")
    media.close()
    if os.path.exists(f"media/{title}"):
        os.remove(f"media/{title}")


@dp.callback_query_handler(text='ytmp3')
async def Admincall(call: CallbackQuery):
    title = dowload_audio(data['meta']['source'])

    audio = open(f'audio/{title}', 'rb')

    await bot.delete_message(call.message.chat.id, call.message.message_id)
    await bot.send_chat_action(call.message.chat.id, 'upload_document')
    await call.message.answer_audio(audio, caption='@Alpha4Groupbot')
    audio.close()

    if os.path.exists(f"audio/{title}"):
        os.remove(f"audio/{title}")
