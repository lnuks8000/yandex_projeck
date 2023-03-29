import telebot
from telebot import types


bot = telebot.TeleBot('6197994890:AAH4gv_1nrvzAGGzQm1OxYKsXumDH9P8FvI')
@bot.message_handler(commands=['start'])
def send_welcome(message):
    #print(message.from_user.id)
    markup = types.ReplyKeyboardMarkup()
    if message.from_user.id in m.keys():
        # Создаем клавиатуру с кнопкой "Расписание"

        itembtn = types.KeyboardButton('Расписание')
        markup.add(itembtn)
        news = types.KeyboardButton('Важные новости')
        markup.add(news)

        # Отправляем приветственное сообщение с клавиатурой
        if message.from_user.id == 1370770852:
            bot.reply_to(message, "Приветствую мой господин", reply_markup=markup)
        else:
            bot.reply_to(message, "Приветствую! Это чат для урегулирования расписания занятий в ДНОЦ (CERC)", reply_markup=markup)
    else:
        bot.reply_to(message, "Увы, но у тебя нет доступа :)", reply_markup=markup)


# Обработка нажатия кнопки "Расписание"
@bot.message_handler(func=lambda message: message.text == 'Расписание')
def send_schedule(message):
    markup = types.ReplyKeyboardMarkup()
    # Отправляем расписание

    itembtn = types.KeyboardButton('Эта неделя')
    markup.add(itembtn)
    news = types.KeyboardButton('Следующая неделя')
    markup.add(news)
    bot.reply_to(message, "в разработке", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Важные новости')
def send_schedule(message):
    bot.reply_to(message, "в разработке")


@bot.message_handler(func=lambda message: message.text == 'Эта неделя')
def send_schedule(message):
    markup = types.ReplyKeyboardMarkup()
    # Отправляем расписание

    d1 = types.KeyboardButton('Понедельник')
    markup.add(d1)
    d2 = types.KeyboardButton('Вторник')
    markup.add(d2)
    d3 = types.KeyboardButton('Среда')
    markup.add(d3)
    d4 = types.KeyboardButton('Четверг')
    markup.add(d4)
    d5 = types.KeyboardButton('Пятьница')
    markup.add(d5)
    d6 = types.KeyboardButton('Суббота')
    markup.add(d6)
    d7 = types.KeyboardButton('Воскресенье')
    markup.add(d7)
    bot.reply_to(message, "в разработке", reply_markup=markup)

m = {1370770852: ['Разработчик', 0]}
bot.polling()
