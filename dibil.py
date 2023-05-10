import aiogram
from config import *
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
bot = aiogram.Bot(token)
dis = aiogram.Dispatcher(bot)

mainMenuInfo_sled = InlineKeyboardMarkup(row_width=2)
b10b333 = InlineKeyboardButton(text="Следующий", callback_data="123ig")
mainMenuInfo_sled.row(b10b333)

@dis.message_handler()
async def start(message):
    await bot.send_photo(chat_id=message.chat.id, photo='https://all-sfp.ru/wp-content/uploads/9/6/6/96621bd6dd53ca8ef923630224cf4f90.jpg',
                         caption='Привет',
                         reply_markup = mainMenuInfo_sled)




@dis.callback_query_handler(lambda c: c.data.startswith("123"))
async  def end(callback):
    print(callback.data)
    await callback.message.edit_media(types.InputMedia(media='https://i.pinimg.com/originals/20/b8/4a/20b84a18f2a9ecb55e1ae522dab79d2f.jpg' ,type='photo', caption='123123'))
    #await callback.message.edit_caption(caption="hi")
aiogram.executor.start_polling(dis, )#skip_updates=True