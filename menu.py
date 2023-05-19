from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from aiogram.utils.callback_data import CallbackData

show_hero_n = CallbackData('hero', 'hero_id', 'tg_user_id')
def make_i_keyboard(ikm:InlineKeyboardMarkup, text, call_data:CallbackData, *args):#args - все нужные значения
    return ikm.add(InlineKeyboardButton(text=text, callback_data=call_data.new(*args)))
ikm = InlineKeyboardMarkup(row_width=1)
#print(ikm := make_i_keyboard(ikm, 'asdasd', show_hero_n, 'a', 'ss'))

def menu_keyboard(l, *args: InlineKeyboardButton):#нормально добавляет готовые кнопки
    ikm = InlineKeyboardMarkup(row_width=l)
    ikm.add(*args)
    return ikm #> InlineKeyboardMarkup

#а эта функция должна сама генерировать и добавлять текс
def make_all(l, *args):#аргс должны принимать
    buttons = []
    for i in args:
        buttons.append(InlineKeyboardButton(text=i[0],callback_data=i[1].new(*i[2])))
    return InlineKeyboardMarkup(row_width=l).add(*buttons)

aaa = CallbackData('s')
bbb = CallbackData('b', 'asd')
ccc = CallbackData('c', 'asd', 'sad')
#ikm = InlineKeyboardMarkup

print(ikm:= make_all(1, ('asd', aaa, ()), ('asd', bbb, (5,)), ('asd', ccc, (11, 123))))
#print(ikm:= make_all1(2, ('asd', aaa, ()), ('asd', bbb, (5,)), ('asd', ccc, (11, 123))))
        #print(*i)#крч вот так будет получаться инфа
    #print(args[2])
    #(text, CallbackData, *args)
#make_all(1,(3, 4, (5, 6, 7)), (6, 7, (8,)))
#InlineKeyboardButton(text='aaa',callback_data='g' )
#ikm = menu_keyboard(2, InlineKeyboardButton(text='aaa',callback_data='g'), InlineKeyboardButton(text='aaa',callback_data='g' ), InlineKeyboardButton(text='aaa',callback_data='g' ))
#print(ikm)
#ikm.add(InlineKeyboardButton(text='aaa',callback_data='g'))
#print(ikm)