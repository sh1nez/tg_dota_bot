import aiogram
from config import *
bot = aiogram.Bot(token)
dis = aiogram.Dispatcher(bot)

@dis.message_handler()
async def asd(message):
    i = aiogram.types.InlineKeyboardMarkup(row_width=1)
    i1 = aiogram.types.InlineKeyboardButton(callback_data='aaa', text='asdasd')
    i.add(i1)
    await bot.send_photo(photo='https://sun9-73.userapi.com/impf/c852120/v852120718/19f318/CruEz08DPeA.jpg?size=0x0&quality=90&proxy=1&sign=adcb69a503ecc1d7e11aad1c848e5a8f&c_uniq_tag=YWNWOu0LU-VMhzR9FPXr7oKYZiSvm6tQS4xofcKpnJs&type=video_thumb',
                chat_id=message.chat.id, reply_markup=i)


@dis.callback_query_handler(lambda c: c.data.startswith('aaa'))
async def a2312(collback):
    await collback.photo.edit_photo(chat_id=collback.message.chat.id, message_id=collback.message.message_id+1, photo='https://i.ytimg.com/vi/Ylz5z8NqXT8/maxresdefault.jpg')
    await collback.message.edit_media('')



    #await bot.
aiogram.executor.start_polling(dis, )#skip_updates=True