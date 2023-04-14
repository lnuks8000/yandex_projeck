import telebot
import os
from telebot import types
import asyncio
from datetime import datetime
import sys


bot = telebot.TeleBot('6197994890:AAH4gv_1nrvzAGGzQm1OxYKsXumDH9P8FvI')
@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
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
                bot.reply_to(message, f"Приветствую, {str(m[message.from_user.id][0])}! Это чат для урегулирования расписания занятий в ДНОЦ (CERC)", reply_markup=markup)
            else:
                bot.reply_to(message, "Приветствую, отбросы общества! Таких людей как вы, еще поискать прийдется! (к стати, даниИл, ты такой один :))", reply_markup=markup)
        else:
            bot.send_message(1370770852, str(message.from_user.id))
            bot.send_message(1370770852, str(message.from_user.username))
            bot.reply_to(message, "Увы, но у вас нет доступа :)")
    except:
        bot.send_message(message.from_user.id, 'Кажется возникла ошибка, она уже направлена разработчику, советуем попробывать перезапустить бота.')
        bot.send_message(1370770852, f'У {m[message.from_user.id][0]} ({message.from_user.id}) ошибка в функции start')

@bot.message_handler(func=lambda message: message.text == 'Добавить id нового пользователя')
def send_schedule(message):
    try:
        if message.from_user.id in m.keys():
            markup = types.ReplyKeyboardMarkup()
            if m[message.from_user.id][1] == 0:
                t = types.KeyboardButton('Назад')
                markup.add(t)
                bot.send_message(message.from_user.id, "Для добавления нового пользователя: введите данные в данном формате:\n'пароль id имя статус'\nпароль вам был сказан Матвеем, если это не так, следует к нему обратиться: @matvey_kirtaev\nкак узнать id можно узнать по сокращенной ссылке пикабу: https://goo.su/fkIxwIc\nимя - имя человека которого вы добавляете\nстатус измеряется от 0 до 1, 0 - более высокая должность, 1 - более низкая должность.", reply_markup=markup)
            else:
                bot.send_message(message.from_user.id, 'Что, думал(-а) самый умный!? Так я это предусмотрел!')
        else:
            bot.reply_to(message, "Увы, но у вас нет доступа :)")
            bot.send_message(1370770852, str(message.from_user.id))
            bot.send_message(1370770852, str(message.from_user.username))
    except:
        bot.send_message(message.from_user.id, 'Кажется возникла ошибка, она уже направлена разработчику, советуем попробывать перезапустить бота.')
        bot.send_message(1370770852, f"У {m[message.from_user.id][0]} ({message.from_user.id}) ошибка в функции 'добавить id'")


@bot.message_handler(func=lambda message: 'future_planet' in message.text)
def send_schedule(message):
    try:
        if message.from_user.id in m.keys() and m[message.from_user.id][1] == 0:
            try:
                x = message.text
                x = x.split()
                m[int(x[1])] = [x[2:-1], int(x[-1])]
                u = open('id.txt', 'r')
                o = u.readlines()
                if ' '.join(x[1:]) not in o:
                    u.close()
                    u = open('id.txt', 'a')
                    u.write('\n' + ' '.join(x[1:]))
                    bot.send_message(message.from_user.id, "Отлично, человек добавлен и может пользоваться сервисом!")
                else:
                    u.close()
                    bot.send_message(message.from_user.id, "У этого человека и так есть доступ.")
            except:
                bot.send_message(message.from_user.id, 'почему-то ошибка, проблема уже отправлена Матвею и чуть-позже он сам добавит пользователя')
        else:
            bot.send_message(message.from_user.id, 'Увы, но у вас не достаточно прав доступа')
            bot.send_message(1370770852, str(message.from_user.id))
            bot.send_message(1370770852, str(message.from_user.username))
    except:
        bot.send_message(message.from_user.id, 'Кажется возникла ошибка, она уже направлена разработчику, советуем попробывать перезапустить бота.')
        bot.send_message(1370770852, f"У {m[message.from_user.id][0]} ({message.from_user.id}) ошибка в функции 'добавить id 2. которая с паролем'")


@bot.message_handler(func=lambda message: message.text == 'Назад')
def nazad(message):
    try:
        if message.from_user.id in m.keys():
            send_welcome(message)
        else:
            bot.reply_to(message, "Увы, но у вас нет доступа :)")
            bot.send_message(1370770852, str(message.from_user.id))
            bot.send_message(1370770852, str(message.from_user.username))
    except:
        bot.send_message(message.from_user.id,  'Кажется возникла ошибка, она уже направлена разработчику, советуем попробывать перезапустить бота.')
        bot.send_message(1370770852, f"У {m[message.from_user.id][0]} ({message.from_user.id}) ошибка в функции 'назад'")


@bot.message_handler(func=lambda message: message.text == 'Расписание')
def send_schedule(message):
    try:
        if message.from_user.id in m.keys():
            markup = types.ReplyKeyboardMarkup()
            # Отправляем расписание

            itembtn = types.KeyboardButton('Эта неделя')
            markup.add(itembtn)
            news = types.KeyboardButton('Следующая неделя')
            markup.add(news)
            bot.reply_to(message, "Выберите неделю", reply_markup=markup)
        else:
            bot.reply_to(message, "Увы, но у вас нет доступа :)")
            bot.send_message(1370770852, str(message.from_user.id))
            bot.send_message(1370770852, str(message.from_user.username))
    except:
        bot.send_message(message.from_user.id, 'Кажется возникла ошибка, она уже направлена разработчику, советуем попробывать перезапустить бота.')
        bot.send_message(1370770852, f"У {m[message.from_user.id][0]} ({message.from_user.id}) ошибка в функции 'расписание'")


@bot.message_handler(func=lambda message: message.text == 'Важные новости')
def newses(message):
    try:
        if message.from_user.id in m.keys():
            global ned, den
            ned = 3
            den = 0
            markup = types.ReplyKeyboardMarkup()
            s = types.KeyboardButton('Назад')
            markup.add(s)
            u = open('ned3/0.txt', 'r')
            x = u.readlines()
            t = ''
            for i in range(len(x)):
                t += f'{i + 1})' + ' '.join(x[i].split()) + '\n'
            if m[message.from_user.id][1] == 0:
                news = types.KeyboardButton('Добавить новость')
                markup.add(news)
                if x:
                    itembtn = types.KeyboardButton('Удалить новость')
                    markup.add(itembtn)
                u.close()
            if x:
                bot.reply_to(message, "Новости:" + '\n' + t, reply_markup=markup)
            else:
                bot.reply_to(message, "Новостей пока нет", reply_markup=markup)
        else:

            bot.reply_to(message, "Увы, но у вас нет доступа :)")
            bot.send_message(1370770852, str(message.from_user.id))
            bot.send_message(1370770852, str(message.from_user.username))
    except:
        e = sys.exc_info()[1]
        bot.send_message(message.from_user.id, 'Кажется возникла ошибка, она уже направлена разработчику, советуем попробывать перезапустить бота.')
        bot.send_message(1370770852, f"У {m[message.from_user.id][0]} ({message.from_user.id}) ошибка в функции 'важные новости'")


@bot.message_handler(func=lambda message: message.text == 'Добавить новость')
def send_schedule(message):
    try:
        if message.from_user.id in m.keys():
            markup = types.ReplyKeyboardMarkup()
            itembtn = types.KeyboardButton('Назад')
            markup.add(itembtn)
            bot.reply_to(message, f"Введите информацию одним сообщением", reply_markup=markup)
            bot.register_next_step_handler(message, ououou)
        else:
            bot.reply_to(message, "Увы, но у вас нет доступа :)")
            bot.send_message(1370770852, str(message.from_user.id))
            bot.send_message(1370770852, str(message.from_user.username))
    except:
        bot.send_message(message.from_user.id, 'Кажется возникла ошибка, она уже направлена разработчику, советуем попробывать перезапустить бота.')
        bot.send_message(1370770852, f"У {m[message.from_user.id][0]} ({message.from_user.id}) ошибка в функции 'добавить запись'")


def ououou(message):
    try:
        if message.from_user.id in m.keys():
            if message.text != 'Назад':
                u = open('ned3/0.txt', 'a')
                x = str(message.text) + '\n'
                u.write(x)
                bot.send_message(message.from_user.id, f"Новость добавлена!")
                #newses(message)
            else:
                nazad(message)
        else:
            bot.reply_to(message, "Увы, но у вас нет доступа :)")
            bot.send_message(1370770852, str(message.from_user.id))
            bot.send_message(1370770852, str(message.from_user.username))
    except:
        bot.send_message(message.from_user.id,
                         'Кажется возникла ошибка, она уже направлена разработчику, советуем попробывать перезапустить бота.')
        bot.send_message(1370770852,
                         f"У {m[message.from_user.id][0]} ({message.from_user.id}) ошибка в функции 'ououou'")

@bot.message_handler(func=lambda message: message.text == 'Удалить новость')
def sew(message):
    try:
        if message.from_user.id in m.keys():
            markup = types.ReplyKeyboardMarkup()
            itembtn = types.KeyboardButton('Назад')
            markup.add(itembtn)
            bot.send_message(message.from_user.id, 'Введите номер новости которую следует удалить', reply_markup=markup)
            bot.register_next_step_handler(message, cat)
        else:
            bot.reply_to(message, "Увы, но у вас нет доступа :)")
            bot.send_message(1370770852, str(message.from_user.id))
            bot.send_message(1370770852, str(message.from_user.username))
    except:
        bot.send_message(message.from_user.id,
                         'Кажется возникла ошибка, она уже направлена разработчику, советуем попробывать перезапустить бота.')
        bot.send_message(1370770852,
                         f"У {m[message.from_user.id][0]} ({message.from_user.id}) ошибка в функции 'Удалить новость'")
def cat(message):
    try:
        if message.from_user.id in m.keys():
            try:
                u = open('ned3/0.txt', 'r')
                x = u.readlines()
                u.close()
                a = int(message.text)
                if 1 <= a <= len(x):
                    u = open('ned3/0.txt', 'w')
                    for i in range(len(x)):
                        if i != a - 1:
                            u.write(x[i])
                    u.close()
                    bot.send_message(message.from_user.id, 'Новость удалена')
                    newses(message)
                else:
                    bot.send_message(message.from_user.id,
                                     'Пожалуйста, проверьте правльность ввода.' + '\n' + 'Число не должно быть меньше или больше возможных')
                    bot.register_next_step_handler(message, cat)
            except:
                bot.send_message(message.from_user.id, 'Пожалуйста, проверьте правльность ввода.' + '\n' + 'Число не должно быть меньше или больше возможных')
        else:
            bot.reply_to(message, "Увы, но у вас нет доступа :)")
            bot.send_message(1370770852, str(message.from_user.id))
            bot.send_message(1370770852, str(message.from_user.username))
    except:
        bot.send_message(message.from_user.id,
                         'Кажется возникла ошибка, она уже направлена разработчику, советуем попробывать перезапустить бота.')
        bot.send_message(1370770852,
                         f"У {m[message.from_user.id][0]} ({message.from_user.id}) ошибка в функции 'Удалить новость'")

@bot.message_handler(func=lambda message: message.text == 'Эта неделя')
def send_schedule(message):
    try:
        if message.from_user.id in m.keys():
            global ned
            ned = 0
            markup = types.ReplyKeyboardMarkup() \
                # Отправляем расписание
            p = datetime.today().isoweekday()
            print(p)
            if p < 1:
                d1 = types.KeyboardButton('Понедельник')
                markup.add(d1)
            if p < 2:
                d2 = types.KeyboardButton('Вторник')
                markup.add(d2)
            if p < 3:
                d3 = types.KeyboardButton('Среда')
                markup.add(d3)
            if p < 4:
                d4 = types.KeyboardButton('Четверг')
                markup.add(d4)
            if p < 5:
                d5 = types.KeyboardButton('Пятница')
                markup.add(d5)
            if p < 6:
                d6 = types.KeyboardButton('Суббота')
                markup.add(d6)
            if p < 7:
                d7 = types.KeyboardButton('Воскресенье')
                markup.add(d7)
            bot.reply_to(message, "Выбирите день", reply_markup=markup)
        else:
            bot.reply_to(message, "Увы, но у вас нет доступа :)")
            bot.send_message(1370770852, str(message.from_user.id))
            bot.send_message(1370770852, str(message.from_user.username))
    except:
        bot.send_message(message.from_user.id, 'Кажется возникла ошибка, она уже направлена разработчику, советуем попробывать перезапустить бота.')
        bot.send_message(1370770852, f"У {m[message.from_user.id][0]} ({message.from_user.id}) ошибка в функции 'эта неделя'")


@bot.message_handler(func=lambda message: message.text == 'Понедельник')
def send_schedule(message):
    try:
        if message.from_user.id in m.keys():
            global den
            den = 1
            markup = types.ReplyKeyboardMarkup()
            pon1 = {}
            u = open(f'ned{ned}/{den}.txt', 'r')
            x = u.readlines()
            try:
                if x:
                    for i in x:
                        f = i.split()
                        print(f)
                        print(f[:-2], f[-2], f[-1])
                        pon1[' '.join(f[:-2])] = [f[-2], f[-1]]
            except:
                e = sys.exc_info()[1]
                print(e.args[0])
                bot.send_message(1370770852, 'балин, опять ошибки посыпались')
                bot.send_message(1370770852, '\n'.join(x))
                bot.send_message(message.from_user.id, 'Извините, кажется что-то случилось, ошибка уже решается')
            u.close()
            itembtn = types.KeyboardButton('Назад')
            markup.add(itembtn)
            if m[message.from_user.id][0] in pon1:
                u = types.KeyboardButton('Удалить запись')
                markup.add(u)
            else:
                u = types.KeyboardButton('Добавить запись')
                markup.add(u)
            soop = ''
            for name, key in pon1.items():
                soop += f"{name}: {' - '.join(key)}" + '\n'
            # u.close()
            if soop != '':
                bot.reply_to(message, f"{soop}", reply_markup=markup)
            else:
                bot.reply_to(message, f"Еще никто не записался.", reply_markup=markup)
        else:
            bot.reply_to(message, "Увы, но у вас нет доступа :)")
            bot.send_message(1370770852, str(message.from_user.id))
            bot.send_message(1370770852, str(message.from_user.username))
    except:
        bot.send_message(message.from_user.id, 'Кажется возникла ошибка, она уже направлена разработчику, советуем попробывать перезапустить бота.')
        bot.send_message(1370770852, f"У {m[message.from_user.id][0]} ({message.from_user.id}) ошибка в функции 'понедельник'")


@bot.message_handler(func=lambda message: message.text == 'Вторник')
def send_schedule(message):
    try:
        if message.from_user.id in m.keys():
            global den
            den = 2
            markup = types.ReplyKeyboardMarkup()
            pon1 = {}
            u = open(f'ned{ned}/{den}.txt', 'r')
            x = u.readlines()
            try:
                if x:
                    for i in x:
                        f = i.split()
                        print(f)
                        print(f[:-2], f[-2], f[-1])
                        pon1[' '.join(f[:-2])] = [f[-2], f[-1]]
            except:
                bot.send_message(1370770852, 'балин, опять ошибки посыпались')
                bot.send_message(1370770852, '\n'.join(x))
                bot.send_message(message.from_user.id, 'Извините, кажется что-то случилось, ошибка уже решается')
            u.close()
            itembtn = types.KeyboardButton('Назад')
            markup.add(itembtn)
            if m[message.from_user.id][0] in pon1:
                u = types.KeyboardButton('Удалить запись')
                markup.add(u)
            else:
                u = types.KeyboardButton('Добавить запись')
                markup.add(u)
            soop = ''
            for name, key in pon1.items():
                soop += f"{name}: {' - '.join(key)}" + '\n'
            # u.close()
            if soop != '':
                bot.reply_to(message, f"{soop}", reply_markup=markup)
            else:
                bot.reply_to(message, f"Еще никто не записался.", reply_markup=markup)
        else:
            bot.reply_to(message, "Увы, но у вас нет доступа :)")
            bot.send_message(1370770852, str(message.from_user.id))
            bot.send_message(1370770852, str(message.from_user.username))
    except:
        bot.send_message(message.from_user.id, 'Кажется возникла ошибка, она уже направлена разработчику, советуем попробывать перезапустить бота.')
        bot.send_message(1370770852, f"У {m[message.from_user.id][0]} ({message.from_user.id}) ошибка в функции 'Вторник'")


@bot.message_handler(func=lambda message: message.text == 'Среда')
def send_schedule(message):
    try:
        if message.from_user.id in m.keys():
            global den
            den = 3
            markup = types.ReplyKeyboardMarkup()
            pon1 = {}
            u = open(f'ned{ned}/{den}.txt', 'r')
            x = u.readlines()
            try:
                if x:
                    for i in x:
                        f = i.split()
                        print(f)
                        print(f[:-2], f[-2], f[-1])
                        pon1[' '.join(f[:-2])] = [f[-2], f[-1]]
            except:
                bot.send_message(1370770852, 'балин, опять ошибки посыпались')
                bot.send_message(1370770852, '\n'.join(x))
                bot.send_message(message.from_user.id, 'Извините, кажется что-то случилось, ошибка уже решается')
            u.close()
            itembtn = types.KeyboardButton('Назад')
            markup.add(itembtn)
            if m[message.from_user.id][0] in pon1:
                u = types.KeyboardButton('Удалить запись')
                markup.add(u)
            else:
                u = types.KeyboardButton('Добавить запись')
                markup.add(u)
            soop = ''
            for name, key in pon1.items():
                soop += f"{name}: {' - '.join(key)}" + '\n'
            # u.close()
            if soop != '':
                bot.reply_to(message, f"{soop}", reply_markup=markup)
            else:
                bot.reply_to(message, f"Еще никто не записался.", reply_markup=markup)
        else:
            bot.reply_to(message, "Увы, но у вас нет доступа :)")
            bot.send_message(1370770852, str(message.from_user.id))
            bot.send_message(1370770852, str(message.from_user.username))
    except:
        bot.send_message(message.from_user.id, 'Кажется возникла ошибка, она уже направлена разработчику, советуем попробывать перезапустить бота.')
        bot.send_message(1370770852, f"У {m[message.from_user.id][0]} ({message.from_user.id}) ошибка в функции 'среда'")


@bot.message_handler(func=lambda message: message.text == 'Четверг')
def send_schedule(message):
    try:
        if message.from_user.id in m.keys():
            global den
            den = 4
            markup = types.ReplyKeyboardMarkup()
            pon1 = {}
            u = open(f'ned{ned}/{den}.txt', 'r')
            x = u.readlines()
            try:
                if x:
                    for i in x:
                        f = i.split()
                        print(f)
                        print(f[:-2], f[-2], f[-1])
                        pon1[' '.join(f[:-2])] = [f[-2], f[-1]]
            except:
                bot.send_message(1370770852, 'балин, опять ошибки посыпались')
                bot.send_message(1370770852, '\n'.join(x))
                bot.send_message(message.from_user.id, 'Извините, кажется что-то случилось, ошибка уже решается')
            u.close()
            itembtn = types.KeyboardButton('Назад')
            markup.add(itembtn)
            if m[message.from_user.id][0] in pon1:
                u = types.KeyboardButton('Удалить запись')
                markup.add(u)
            else:
                u = types.KeyboardButton('Добавить запись')
                markup.add(u)
            soop = ''
            for name, key in pon1.items():
                soop += f"{name}: {' - '.join(key)}" + '\n'
            # u.close()
            if soop != '':
                bot.reply_to(message, f"{soop}", reply_markup=markup)
            else:
                bot.reply_to(message, f"Еще никто не записался.", reply_markup=markup)
        else:
            bot.reply_to(message, "Увы, но у вас нет доступа :)")
            bot.send_message(1370770852, str(message.from_user.id))
            bot.send_message(1370770852, str(message.from_user.username))
    except:
        bot.send_message(message.from_user.id, 'Кажется возникла ошибка, она уже направлена разработчику, советуем попробывать перезапустить бота.')
        bot.send_message(1370770852, f"У {m[message.from_user.id][0]} ({message.from_user.id}) ошибка в функции 'четверг'")


@bot.message_handler(func=lambda message: message.text == 'Пятница')
def send_schedule(message):
    try:
        if message.from_user.id in m.keys():
            global den
            den = 5
            markup = types.ReplyKeyboardMarkup()
            pon1 = {}
            u = open(f'ned{ned}/{den}.txt', 'r')
            x = u.readlines()
            try:
                if x:
                    for i in x:
                        f = i.split()
                        print(f)
                        print(f[:-2], f[-2], f[-1])
                        pon1[' '.join(f[:-2])] = [f[-2], f[-1]]
            except:
                e = sys.exc_info()[1]
                print(e)
                bot.send_message(1370770852, 'балин, опять ошибки посыпались')
                bot.send_message(1370770852, '\n'.join(x))
                bot.send_message(message.from_user.id, 'Извините, кажется что-то случилось, ошибка уже решается')
            u.close()
            itembtn = types.KeyboardButton('Назад')
            markup.add(itembtn)
            if m[message.from_user.id][0] in pon1:
                u = types.KeyboardButton('Удалить запись')
                markup.add(u)
            else:
                u = types.KeyboardButton('Добавить запись')
                markup.add(u)
            soop = ''
            for name, key in pon1.items():
                soop += f"{name}: {' - '.join(key)}" + '\n'
            # u.close()
            if soop != '':
                bot.reply_to(message, f"{soop}", reply_markup=markup)
            else:
                bot.reply_to(message, f"Еще никто не записался.", reply_markup=markup)
        else:
            bot.reply_to(message, "Увы, но у вас нет доступа :)")
            bot.send_message(1370770852, str(message.from_user.id))
            bot.send_message(1370770852, str(message.from_user.username))
    except:
        bot.send_message(message.from_user.id, 'Кажется возникла ошибка, она уже направлена разработчику, советуем попробывать перезапустить бота.')
        bot.send_message(1370770852, f"У {m[message.from_user.id][0]} ({message.from_user.id}) ошибка в функции 'пятьница'")


@bot.message_handler(func=lambda message: message.text == 'Суббота')
def send_schedule(message):
    try:
        if message.from_user.id in m.keys():
            global den
            den = 6
            markup = types.ReplyKeyboardMarkup()
            pon1 = {}
            u = open(f'ned{ned}/{den}.txt', 'r')
            x = u.readlines()
            try:
                if x:
                    for i in x:
                        f = i.split()
                        print(f)
                        print(f[:-2], f[-2], f[-1])
                        pon1[' '.join(f[:-2])] = [f[-2], f[-1]]
            except:
                bot.send_message(1370770852, 'балин, опять ошибки посыпались')
                bot.send_message(1370770852, '\n'.join(x))
                bot.send_message(message.from_user.id, 'Извините, кажется что-то случилось, ошибка уже решается')
            u.close()
            itembtn = types.KeyboardButton('Назад')
            markup.add(itembtn)
            if m[message.from_user.id][0] in pon1:
                u = types.KeyboardButton('Удалить запись')
                markup.add(u)
            else:
                u = types.KeyboardButton('Добавить запись')
                markup.add(u)
            soop = ''
            for name, key in pon1.items():
                soop += f"{name}: {' - '.join(key)}" + '\n'
            # u.close()
            if soop != '':
                bot.reply_to(message, f"{soop}", reply_markup=markup)
            else:
                bot.reply_to(message, f"Еще никто не записался.", reply_markup=markup)
        else:
            bot.reply_to(message, "Увы, но у вас нет доступа :)")
            bot.send_message(1370770852, str(message.from_user.id))
            bot.send_message(1370770852, str(message.from_user.username))
    except:
        bot.send_message(message.from_user.id, 'Кажется возникла ошибка, она уже направлена разработчику, советуем попробывать перезапустить бота.')
        bot.send_message(1370770852, f"У {m[message.from_user.id][0]} ({message.from_user.id}) ошибка в функции 'суббота'")


@bot.message_handler(func=lambda message: message.text == 'Воскресенье')
def send_schedule(message):
    try:
        if message.from_user.id in m.keys():
            global den
            den = 7
            markup = types.ReplyKeyboardMarkup()
            pon1 = {}
            u = open(f'ned{ned}/{den}.txt', 'r')
            x = u.readlines()
            try:
                if x:
                    for i in x:
                        f = i.split()
                        print(f)
                        print(f[:-2], f[-2], f[-1])
                        pon1[' '.join(f[:-2])] = [f[-2], f[-1]]
            except:
                bot.send_message(1370770852, 'балин, опять ошибки посыпались')
                bot.send_message(1370770852, '\n'.join(x))
                bot.send_message(message.from_user.id, 'Извините, кажется что-то случилось, ошибка уже решается')
            u.close()
            itembtn = types.KeyboardButton('Назад')
            markup.add(itembtn)
            if m[message.from_user.id][0] in pon1:
                u = types.KeyboardButton('Удалить запись')
                markup.add(u)
            else:
                u = types.KeyboardButton('Добавить запись')
                markup.add(u)
            soop = ''
            for name, key in pon1.items():
                soop += f"{name}: {' - '.join(key)}" + '\n'
            # u.close()
            if soop != '':
                bot.reply_to(message, f"{soop}", reply_markup=markup)
            else:
                bot.reply_to(message, f"Еще никто не записался.", reply_markup=markup)
        else:
            bot.reply_to(message, "Увы, но у вас нет доступа :)")
            bot.send_message(1370770852, str(message.from_user.id))
            bot.send_message(1370770852, str(message.from_user.username))
    except:
        bot.send_message(message.from_user.id, 'Кажется возникла ошибка, она уже направлена разработчику, советуем попробывать перезапустить бота.')
        bot.send_message(1370770852, f"У {m[message.from_user.id][0]} ({message.from_user.id}) ошибка в функции 'воскресенье'")


@bot.message_handler(func=lambda message: message.text == 'Удалить запись')
def send_schedule(message):
    try:
        if message.from_user.id in m.keys():
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
        else:
            bot.reply_to(message, "Увы, но у вас нет доступа :)")
            bot.send_message(1370770852, str(message.from_user.id))
            bot.send_message(1370770852, str(message.from_user.username))
    except:
        bot.send_message(message.from_user.id, 'Кажется возникла ошибка, она уже направлена разработчику, советуем попробывать перезапустить бота.')
        bot.send_message(1370770852, f"У {m[message.from_user.id][0]} ({message.from_user.id}) ошибка в функции 'удалить запись'")


@bot.message_handler(func=lambda message: message.text == 'Добавить запись')
def send_schedule(message):
    try:
        if message.from_user.id in m.keys():
            markup = types.ReplyKeyboardMarkup()
            itembtn = types.KeyboardButton('Назад')
            markup.add(itembtn)
            bot.reply_to(message,
                         f"Время посещения в формате: 'чч.мм-чч.мм'",
                         reply_markup=markup)
            bot.register_next_step_handler(message, rech)
        else:
            bot.reply_to(message, "Увы, но у вас нет доступа :)")
            bot.send_message(1370770852, str(message.from_user.id))
            bot.send_message(1370770852, str(message.from_user.username))
    except:
        bot.send_message(message.from_user.id, 'Кажется возникла ошибка, она уже направлена разработчику, советуем попробывать перезапустить бота.')
        bot.send_message(1370770852, f"У {m[message.from_user.id][0]} ({message.from_user.id}) ошибка в функции 'добавить запись'")

#@bot.message_handler(func=lambda message: message.text[0] == '#')
def rech(message):
    try:
        if message.from_user.id in m.keys():
            if message.text != 'Назад':
                markup = types.ReplyKeyboardMarkup()
                x = message.text
                if '-' in x:
                    x = ' '.join(x.split('-'))
                    u = open(f'ned{ned}/{den}.txt', 'a')
                    u.write(f"{m[message.from_user.id][0]} {x}")
                    bot.reply_to(message, 'Запись добавлена')
                else:
                    bot.reply_to(message, 'Неправильный формат ввода')
                    bot.register_next_step_handler(message, rech)
            else:
                nazad(message)
        else:
            bot.reply_to(message, "Увы, но у вас нет доступа :)")
            bot.send_message(1370770852, str(message.from_user.id))
            bot.send_message(1370770852, str(message.from_user.username))
    except:
        bot.send_message(message.from_user.id, 'Кажется возникла ошибка, она уже направлена разработчику, советуем попробывать перезапустить бота.')
        bot.send_message(1370770852, f"У {m[message.from_user.id][0]} ({message.from_user.id}) ошибка в функции '#'")

@bot.message_handler(func=lambda message: message.text == 'Следующая неделя')
def send_schedule(message):
    try:
        if message.from_user.id in m.keys():
            global ned
            ned = 1
            markup = types.ReplyKeyboardMarkup() \
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
        else:
            bot.reply_to(message, "Увы, но у вас нет доступа :)")
            bot.send_message(1370770852, str(message.from_user.id))
            bot.send_message(1370770852, str(message.from_user.username))
    except:
        bot.send_message(message.from_user.id, 'Кажется возникла ошибка, она уже направлена разработчику, советуем попробывать перезапустить бота.')
        bot.send_message(1370770852, f"У {m[message.from_user.id][0]} ({message.from_user.id}) ошибка в функции 'следующая неделя'")


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
#os.startfile(r'update.py')
bot.polling()
