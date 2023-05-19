host = 'localhost'
user = 'root'
password = ''
db_name = 'test_bot'
token = '6241515938:AAHRAYFoUP7oWDMqJ4pEynnB0OWp6CBlq8k'

# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from texts import item_dick
# from aiogram.utils.callback_data import CallbackData
# look_at_item = CallbackData('a', 's', 'asd')
# #########до
# her = len(item_dick)
# ikm = InlineKeyboardMarkup(row_width=her+1)
# for i in range(0, her, 2):
#     try:
#         ikm.add(InlineKeyboardButton(text=item_dick[i]['name'], callback_data=look_at_item.new(i)),
#             InlineKeyboardButton(text=item_dick[i+1]['name'], callback_data=look_at_item.new(i+1)))
#         #print('lj,fdbk')
#     except:
#         try:
#             ikm.add(
#                 InlineKeyboardButton(text=item_dick[i]['name'], callback_data=item_dick.new(i)))
#             #print('hui')
#         except:
#             #print('(((')
#             break
####ПОСЛЕ

#функция
# def make_all(l, *args):#передать инфу в формате n, (text, CallbackData, *args)
#     buttons = []
#     for i in args:
#         buttons.append(InlineKeyboardButton(text=i[0],callback_data=i[1].new(*i[2])))
#     return InlineKeyboardMarkup(row_width=l).add(*buttons)
#использование
#tup = tuple((item_dick['farm'][i]['name'],look_at_item, (1,2)) for i in item_dick['farm'])
#ikm = make_all(2, *tup)
