from telebot import types

def Start(bot, message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Проходные баллы")
    item2 = types.KeyboardButton("Список экзаменов")
    item3 = types.KeyboardButton("Списки поступивших")
    item4 = types.KeyboardButton("Прочее")
    item5 = types.KeyboardButton("Контакты")

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id,
                     "Рад приветствовать {0.first_name}!\nЯ бот-помощник по теме абитуриентов Сибирского Государственного Университета Геосистем и Технологий.\nПостараюсь ответить на все интересующие Вас вопросы.".format(
                     message.from_user, bot.get_me()), reply_markup=markup)