import telebot
from telebot import types
import this_ned
import future_ned


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
        bot.send_message(1370770852, str(message.from_user.id))
        bot.send_message(1370770852, str(message.from_user.username))
        bot.reply_to(message, "Увы, но у вас нет доступа :)", reply_markup=markup)


# Обработка нажатия кнопки "Расписание"
@bot.message_handler(func=lambda message: message.text == 'Расписание')
def send_schedule(message):
    markup = types.ReplyKeyboardMarkup()
    # Отправляем расписание

    itembtn = types.KeyboardButton('Эта неделя')
    markup.add(itembtn)
    news = types.KeyboardButton('Следующая неделя')
    markup.add(news)
    bot.reply_to(message, "Выбирите неделю", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Важные новости')
def send_schedule(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn = types.KeyboardButton('Назад')
    markup.add(itembtn)
    bot.reply_to(message, "Новости", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Эта неделя')
def send_schedule(message):
    ned = 0
    markup = types.ReplyKeyboardMarkup()\
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
    bot.reply_to(message, "Выбирите день", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Понедельник')
def send_schedule(message):
    markup = types.ReplyKeyboardMarkup()
    if ned == 0:
        itembtn = types.KeyboardButton('Назад')
        markup.add(itembtn)
        if m[message.from_user.id][0] in pon1:
            u = types.KeyboardButton('Удалить записть')
            markup.add(u)
        else:
            u = types.KeyboardButton('Добавить записть')
            markup.add(u)
        for name, key in pon1.items():
            bot.reply_to(message, f"{name}: {' '.join(key)}")
        bot.reply_to(message, "Расписание на понедельник", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Следующая неделя')
def send_schedule(message):
    ned = 1
    markup = types.ReplyKeyboardMarkup()\
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
    bot.reply_to(message, "Выбирите день", reply_markup=markup)


m = {1370770852: ['Разработчик', 0],
     374752561: ['Евгений Александрович', 0],
     974221395: ['Даниил', 2],
     1755954128: ['Тимофей', 1],
     817689430: ['Вераника', 1]}
ned = 0

pon1 = {'Разработчик': ['6.00', '7.00']}
vtor1 = []
sred1 = []
chet1 = []
pyt1 = []
subb1 = []
vosk1 = []
pon2 = []
vtor2 = []
sred2 = []
chet2 = []
pyt2 = []
subb2 = []
vosk2 = []

#ctrl_z = 0
bot.polling()
