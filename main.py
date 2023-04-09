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
            bot.reply_to(message, f"Приветствую, {m[message.from_user.id][0]}! Это чат для урегулирования расписания занятий в ДНОЦ (CERC)", reply_markup=markup)
    else:
        bot.send_message(1370770852, str(message.from_user.id))
        bot.send_message(1370770852, str(message.from_user.username))
        bot.reply_to(message, "Увы, но у вас нет доступа :)", reply_markup=markup)

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
    markup = types.ReplyKeyboardMarkup()
    if ned == 0:
        pon1 = {}
        u = open('pon1.txt', 'r')
        x = u.readlines()
        for i in x:
            a, b, c = i.split()
            pon1[a] = [b, c]
        u.close()
        itembtn = types.KeyboardButton('Назад')
        markup.add(itembtn)
        if m[message.from_user.id][0] in pon1:
            u = types.KeyboardButton('Удалить записть на этот понедельник')
            markup.add(u)
        else:
            u = types.KeyboardButton('Добавить записть на этот понедельник')
            markup.add(u)
        soop = ''
        for name, key in pon1.items():
            soop += f"{name}: {' - '.join(key)}" + '\n'
        #u.close()
        if soop != '':
            bot.reply_to(message, f"{soop}", reply_markup=markup)
        else:
            bot.reply_to(message, f"Еще никто не записался.", reply_markup=markup)
    else:
        pon2 = {}
        u = open('pon2.txt', 'r')
        x = u.readlines()
        for i in x:
            a, b, c = i.split()
            pon2[a] = [b, c]
        u.close()
        itembtn = types.KeyboardButton('Назад')
        markup.add(itembtn)
        if m[message.from_user.id][0] in pon2:
            u = types.KeyboardButton('Удалить записть на следующий понедельник')
            markup.add(u)
        else:
            u = types.KeyboardButton('Добавить записть на следующий понедельник')
            markup.add(u)
        soop = ''
        for name, key in pon2.items():
            soop += f"{name}: {' - '.join(key)}" + '\n'
        # u.close()
        if soop != '':
            bot.reply_to(message, f"{soop}", reply_markup=markup)
        else:
            bot.reply_to(message, f"Еще никто не записался.", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Удалить записть на этот понедельник')
def send_schedule(message):
    markup = types.ReplyKeyboardMarkup()
    if ned == 0:
        u = open('pon1.txt', 'r')
        x = u.readlines()
        y = []
        for i in x:
            if m[message.from_user.id][0] not in i:
                y.append(i)
        u.close()
        u = open('pon1.txt', 'w')
        u.write('\n'.join(y))
        u.close()
    else:
        u = open('pon2.txt', 'r')
        x = u.readlines()
        y = []
        for i in x:
            if m[message.from_user.id][0] not in i:
                y.append(i)
        u.close()
        u = open('pon1.txt', 'w')
        u.write('\n'.join(y))
        u.close()
    itembtn = types.KeyboardButton('Назад')
    markup.add(itembtn)
    bot.reply_to(message, f"Запись удалена", reply_markup=markup)





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


m = {1370770852: ['Разработчик', 0],
     374752561: ['Евгений Александрович', 0],
     974221395: ['Даниил', 2],
     1755954128: ['Тимофей', 1],
     817689430: ['Вероника', 1],
     1332688273: ['Арсений', 1],
     1206662880: ['Илья', 1],
     849839122: ['Роберт', 1]}
ned = 0
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
