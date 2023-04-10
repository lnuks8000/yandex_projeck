import telebot
import os
from telebot import types
import asyncio
from datetime import datetime


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
        if message.from_user.id == 1370770852 or m[message.from_user.id][1] == 0:
            t = types.KeyboardButton('Добавить id нового пользователя')
            markup.add(t)
            bot.reply_to(message, "Приветствую мой господин", reply_markup=markup)
        elif m[message.from_user.id][1] == 1:
            bot.reply_to(message, f"Приветствую, {m[message.from_user.id][0]}! Это чат для урегулирования расписания занятий в ДНОЦ (CERC)", reply_markup=markup)
        else:
            bot.reply_to(message, "Приветствую, отбросы общества! Таких людей как вы, еще поискать прийдется! (к стати, даниИл, ты такой один :))", reply_markup=markup)
    else:
        bot.send_message(1370770852, str(message.from_user.id))
        bot.send_message(1370770852, str(message.from_user.username))
        bot.reply_to(message, "Увы, но у вас нет доступа :)", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Добавить id нового пользователя')
def send_schedule(message):
    markup = types.ReplyKeyboardMarkup()
    if m[message.from_user.id][1] == 0:
        t = types.KeyboardButton('Назад')
        markup.add(t)
        bot.send_message(message.from_user.id, "Для добавления нового пользователя: введите данные в данном формате:\n'пароль id имя статус'\nпароль вам был сказан Матвеем, если это не так, следует к нему обратиться: @matvey_kirtaev\nкак узнать id можно узнать по сокращенной ссылке пикабу: https://goo.su/fkIxwIc\nимя - имя человека которого вы добавляете\nстатус измеряется от 0 до 1, 0 - более высокая должность, 1 - более низкая должность.", reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'Что, думал(-а) самый умный!? Так я это предусмотрел!')

@bot.message_handler(func=lambda message: 'future_planet' in message.text)
def send_schedule(message):
    try:
        x = message.text
        x = x.split()
        m[int(x[1])] = [x[2:-1], int(x[-1])]
        u = open('id.txt', 'a')
        u.write('\n' + ' '.join(x[1:]))
        bot.send_message(message.from_user.id, "Отлично, человек добавлен и может пользоваться сервисом!")
    except:
        bot.send_message(message.from_user.id, 'почему-то ошибка, проблема уже отправлена Матвею и чуть-позже он сам добавит пользователя')


@bot.message_handler(func=lambda message: message.text == 'Назад')
def send_schedule(message):
    send_welcome(message)

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
    global ned
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
    den = 1
    markup = types.ReplyKeyboardMarkup()
    pon1 = {}
    u = open(f'ned{ned}/{den}.txt', 'r')
    #print(f'ned{ned}/{den}.txt')
    x = u.readlines()
    try:
        for i in x:
            a, b, c = i.split()
            pon1[a] = [b, c]
    except:
        bot.send_message(1370770852, 'балин, опять ошибки посыпались')
        bot.send_message(1370770852, '\n'.join(x))
        bot.send_message(message.from_user.id, 'Извините, кажется что-то случилось, ошибка уже решается')
    u.close()
    itembtn = types.KeyboardButton('Назад')
    markup.add(itembtn)
    if m[message.from_user.id][0] in pon1:
        u = types.KeyboardButton('Удалить записть')
        markup.add(u)
    else:
        u = types.KeyboardButton('Добавить записть')
        markup.add(u)
    soop = ''
    for name, key in pon1.items():
        soop += f"{name}: {' - '.join(key)}" + '\n'
    #u.close()
    if soop != '':
        bot.reply_to(message, f"{soop}", reply_markup=markup)
    else:
        bot.reply_to(message, f"Еще никто не записался.", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Вторник')
def send_schedule(message):
    den = 2
    markup = types.ReplyKeyboardMarkup()
    pon1 = {}
    u = open(f'ned{ned}/{den}.txt', 'r')
    print(f'ned{ned}/{den}.txt')
    x = u.readlines()
    try:
        for i in x:
            a, b, c = i.split()
            pon1[a] = [b, c]
    except:
        bot.send_message(1370770852, 'балин, опять ошибки посыпались')
        bot.send_message(1370770852, '\n'.join(x))
        bot.send_message(message.from_user.id, 'Извините, кажется что-то случилось, ошибка уже решается')
    u.close()
    itembtn = types.KeyboardButton('Назад')
    markup.add(itembtn)
    if m[message.from_user.id][0] in pon1:
        u = types.KeyboardButton('Удалить записть')
        markup.add(u)
    else:
        u = types.KeyboardButton('Добавить записть')
        markup.add(u)
    soop = ''
    for name, key in pon1.items():
        soop += f"{name}: {' - '.join(key)}" + '\n'
    #u.close()
    if soop != '':
        bot.reply_to(message, f"{soop}", reply_markup=markup)
    else:
        bot.reply_to(message, f"Еще никто не записался.", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Среда')
def send_schedule(message):
    den = 3
    markup = types.ReplyKeyboardMarkup()
    pon1 = {}
    u = open(f'ned{ned}/{den}.txt', 'r')
    print(f'ned{ned}/{den}.txt')
    x = u.readlines()
    try:
        for i in x:
            a, b, c = i.split()
            pon1[a] = [b, c]
    except:
        bot.send_message(1370770852, 'балин, опять ошибки посыпались')
        bot.send_message(1370770852, '\n'.join(x))
        bot.send_message(message.from_user.id, 'Извините, кажется что-то случилось, ошибка уже решается')
    u.close()
    itembtn = types.KeyboardButton('Назад')
    markup.add(itembtn)
    if m[message.from_user.id][0] in pon1:
        u = types.KeyboardButton('Удалить записть')
        markup.add(u)
    else:
        u = types.KeyboardButton('Добавить записть')
        markup.add(u)
    soop = ''
    for name, key in pon1.items():
        soop += f"{name}: {' - '.join(key)}" + '\n'
    #u.close()
    if soop != '':
        bot.reply_to(message, f"{soop}", reply_markup=markup)
    else:
        bot.reply_to(message, f"Еще никто не записался.", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Четверг')
def send_schedule(message):
    den = 4
    markup = types.ReplyKeyboardMarkup()
    pon1 = {}
    u = open(f'ned{ned}/{den}.txt', 'r')
    print(f'ned{ned}/{den}.txt')
    x = u.readlines()
    try:
        for i in x:
            a, b, c = i.split()
            pon1[a] = [b, c]
    except:
        bot.send_message(1370770852, 'балин, опять ошибки посыпались')
        bot.send_message(1370770852, '\n'.join(x))
        bot.send_message(message.from_user.id, 'Извините, кажется что-то случилось, ошибка уже решается')
    u.close()
    itembtn = types.KeyboardButton('Назад')
    markup.add(itembtn)
    if m[message.from_user.id][0] in pon1:
        u = types.KeyboardButton('Удалить записть')
        markup.add(u)
    else:
        u = types.KeyboardButton('Добавить записть')
        markup.add(u)
    soop = ''
    for name, key in pon1.items():
        soop += f"{name}: {' - '.join(key)}" + '\n'
    #u.close()
    if soop != '':
        bot.reply_to(message, f"{soop}", reply_markup=markup)
    else:
        bot.reply_to(message, f"Еще никто не записался.", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Пятница')
def send_schedule(message):
    den = 5
    markup = types.ReplyKeyboardMarkup()
    pon1 = {}
    u = open(f'ned{ned}/{den}.txt', 'r')
    print(f'ned{ned}/{den}.txt')
    x = u.readlines()
    try:
        for i in x:
            a, b, c = i.split()
            pon1[a] = [b, c]
    except:
        bot.send_message(1370770852, 'балин, опять ошибки посыпались')
        bot.send_message(1370770852, '\n'.join(x))
        bot.send_message(message.from_user.id, 'Извините, кажется что-то случилось, ошибка уже решается')
    u.close()
    itembtn = types.KeyboardButton('Назад')
    markup.add(itembtn)
    if m[message.from_user.id][0] in pon1:
        u = types.KeyboardButton('Удалить записть')
        markup.add(u)
    else:
        u = types.KeyboardButton('Добавить записть')
        markup.add(u)
    soop = ''
    for name, key in pon1.items():
        soop += f"{name}: {' - '.join(key)}" + '\n'
    #u.close()
    if soop != '':
        bot.reply_to(message, f"{soop}", reply_markup=markup)
    else:
        bot.reply_to(message, f"Еще никто не записался.", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Суббота')
def send_schedule(message):
    den = 6
    markup = types.ReplyKeyboardMarkup()
    pon1 = {}
    u = open(f'ned{ned}/{den}.txt', 'r')
    print(f'ned{ned}/{den}.txt')
    x = u.readlines()
    try:
        for i in x:
            a, b, c = i.split()
            pon1[a] = [b, c]
    except:
        bot.send_message(1370770852, 'балин, опять ошибки посыпались')
        bot.send_message(1370770852, '\n'.join(x))
        bot.send_message(message.from_user.id, 'Извините, кажется что-то случилось, ошибка уже решается')
    u.close()
    itembtn = types.KeyboardButton('Назад')
    markup.add(itembtn)
    if m[message.from_user.id][0] in pon1:
        u = types.KeyboardButton('Удалить записть')
        markup.add(u)
    else:
        u = types.KeyboardButton('Добавить записть')
        markup.add(u)
    soop = ''
    for name, key in pon1.items():
        soop += f"{name}: {' - '.join(key)}" + '\n'
    #u.close()
    if soop != '':
        bot.reply_to(message, f"{soop}", reply_markup=markup)
    else:
        bot.reply_to(message, f"Еще никто не записался.", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Воскресенье')
def send_schedule(message):
    den = 7
    markup = types.ReplyKeyboardMarkup()
    pon1 = {}
    u = open(f'ned{ned}/{den}.txt', 'r')
    print(f'ned{ned}/{den}.txt')
    x = u.readlines()
    try:
        for i in x:
            a, b, c = i.split()
            pon1[a] = [b, c]
    except:
        bot.send_message(1370770852, 'балин, опять ошибки посыпались')
        bot.send_message(1370770852, '\n'.join(x))
        bot.send_message(message.from_user.id, 'Извините, кажется что-то случилось, ошибка уже решается')
    u.close()
    itembtn = types.KeyboardButton('Назад')
    markup.add(itembtn)
    if m[message.from_user.id][0] in pon1:
        u = types.KeyboardButton('Удалить записть')
        markup.add(u)
    else:
        u = types.KeyboardButton('Добавить записть')
        markup.add(u)
    soop = ''
    for name, key in pon1.items():
        soop += f"{name}: {' - '.join(key)}" + '\n'
    #u.close()
    if soop != '':
        bot.reply_to(message, f"{soop}", reply_markup=markup)
    else:
        bot.reply_to(message, f"Еще никто не записался.", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Удалить записть')
def send_schedule(message):
    markup = types.ReplyKeyboardMarkup()
    u = open(f'ned{ned}/{den}.txt', 'r')
    x = u.readlines()
    y = []
    for i in x:
        if m[message.from_user.id][0] not in i:
            y.append(i)
    u.close()
    u = open(f'ned{ned}/{den}.txt', 'w')
    u.write('\n'.join(y))
    u.close()
    itembtn = types.KeyboardButton('Назад')
    markup.add(itembtn)
    bot.reply_to(message, f"Запись удалена", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Добавить записть')
def send_schedule(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn = types.KeyboardButton('Назад')
    markup.add(itembtn)
    bot.reply_to(message, f"Введите время со скольки до скольки вы будете находиться в ДНОЦ в формате: '#15.20 17.00'", reply_markup=markup)


@bot.message_handler(func=lambda message: '#' in message.text)
def send_schedule(message):
    markup = types.ReplyKeyboardMarkup()
    x = message.text[1:-1]
    if ' ' in  x:
        u = open(f'ned{ned}/{den}.txt', 'a')
        u.write(f"{m[message.from_user.id][0]} {x}")
        bot.reply_to(message, 'Запись добавлена')
    else:
        bot.reply_to(message, 'Неправильный формат ввода')



@bot.message_handler(func=lambda message: message.text == 'Следующая неделя')
def send_schedule(message):
    global ned
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


m = {}
u = open('id.txt', 'r')
x = u.readlines()
for i in x:
    k = i.split()
    a = k[0]
    c = k[-1]
    b = ' '.join(k[1:-1])
    m[int(a)] = [b, int(c)]
u.close()
ned = 0
den = 1
os.startfile(r'update.py')
bot.polling()
