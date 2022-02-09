import telebot
from telebot import types

bot = telebot.TeleBot("5062542625:AAGZzyL_4dTwinsm-VnSqq9MAy9_auvbIHY", parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    image = open('index.jpeg', 'rb')
    bot.send_photo(message.chat.id, image)

    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Ноутбуки')
    itembtn2 = types.KeyboardButton('Стационарки')

    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id,
                     "Выберите компьютер: ",
                     reply_markup=markup)

@bot.message_handler(content_types=['text'])
def answer(message):

    if message.text == 'Ноутбуки':
        markup = types.InlineKeyboardMarkup(row_width=2)
        nout1 = telebot.types.InlineKeyboardButton("Macbook",  callback_data = 'mac')
        nout2 = telebot.types.InlineKeyboardButton("Dell inspiron", callback_data = 'dell')
        nout3 = telebot.types.InlineKeyboardButton("Lenovo", callback_data = 'lenovo')
        nout4 = telebot.types.InlineKeyboardButton("Acer", callback_data = 'acer')
        nout5 = telebot.types.InlineKeyboardButton("HP", callback_data = 'hp')
        markup.add(nout1, nout2, nout5, nout4, nout3)
        bot.send_message(message.chat.id,
                         "Выберите какой нутбук",
                         reply_markup=markup)
    if message.text == 'Стационарки':
        markup = types.InlineKeyboardMarkup(row_width=2)
        comp1 = telebot.types.InlineKeyboardButton("ASUS", callback_data='asus')
        comp2 = telebot.types.InlineKeyboardButton("INTEL", callback_data='intel')
        comp3 = telebot.types.InlineKeyboardButton("AMD", callback_data='amd')
        markup.add(comp1,comp2,comp3)
        bot.send_message(message.chat.id,
                         "Выберите комп",
                         reply_markup=markup)

    else:
        bot.send_message(message.chat.id,
                         "Обратитесь к консультанту")



@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    try:
        if call.message:
            if call.data == 'mac':
                bot.send_message(call.message.chat.id, '1050$')
            if call.data == 'dell':
                bot.send_message(call.message.chat.id, '850$')
            if call.data == 'lenovo':
                bot.send_message(call.message.chat.id, '500$')
            if call.data == 'acer':
                bot.send_message(call.message.chat.id, '350$')
            if call.data == 'hp':
                bot.send_message(call.message.chat.id, '150$')
            if call.data == 'asus':
                bot.send_message(call.message.chat.id, 'Intel I5 10 gen, RADEON 5400 price:1050$')
            if call.data == 'intel':
                bot.send_message(call.message.chat.id, 'Intel I7 11 gen, GTX 3070ti price: 1500$')
            if call.data == 'amd':
                bot.send_message(call.message.chat.id, 'Amd ryzen 7 3gen, RADEON 4800 price:1300$')
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id
            )
    except:
        print('error')
bot.polling(none_stop=True)