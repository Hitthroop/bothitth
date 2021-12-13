import random

from telebot import types

def ReadText(bot, message):
    if message.chat.type == 'private':
        if HasString(message.text, "балл"):
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Картография и геоинформатика", callback_data='ball_1')
            item2 = types.InlineKeyboardButton("Экология и природопользование", callback_data='ball_2')
            item3 = types.InlineKeyboardButton("Информационные системы и технологии", callback_data='ball_3')
            item4 = types.InlineKeyboardButton("информационная безопасность", callback_data='ball_4')
            item5 = types.InlineKeyboardButton("Приборостроение", callback_data='ball_5')
            item6 = types.InlineKeyboardButton("Оптотехника", callback_data='ball_6')
            item7 = types.InlineKeyboardButton("Землеустройство и кадастры", callback_data='ball_7')
            item8 = types.InlineKeyboardButton("Геодезия и дистанционное зондирование", callback_data='ball_8')
            item9 = types.InlineKeyboardButton("Стандартизация и метрология", callback_data='ball_9')
            item10 = types.InlineKeyboardButton("Инноватика", callback_data='ball_10')
            item11 = types.InlineKeyboardButton("Прикладная геодезия", callback_data='ball_11')
            item12 = types.InlineKeyboardButton("Горное дело", callback_data='ball_12')

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)

            bot.send_message(message.chat.id, 'Выберите нужное вам направление:', reply_markup=markup)
            bot.send_message(message.chat.id, 'Если вашего направления нет в списке, то их можно посмотреть здесь:\nhttps://sgugit.ru/abitur/bachelor/#abitur_plan_priema')

        elif HasString(message.text, "экзамен") or HasString(message.text, "вступительны"):
            bot.send_message(message.chat.id, 'Ознакомиться с перечнем вступительных испытаний можно здесь:\nhttps://sgugit.ru/abitur/bachelor/#abitur_vstupitelnye-ispytania')

        elif HasString(message.text, "поступивш"):
            bot.send_message(message.chat.id,'Посмотреть полные списки поступающих можно здесь:\nhttps://sgugit.ru/abitur/bachelor/#abitur_spiski-postupayushchih')

        elif HasString(message.text, "информация") or HasString(message.text, "приемн") or HasString(message.text, "комисс") or HasString(message.text, "телефон") or HasString(message.text, "почт") or HasString(message.text, "контак"):
            bot.send_message(message.chat.id,'Информация о приемной комиссии:\nТелефоны: +7 (383) 343-37-01, +7-913-205-75-81\nE-mail: priem.com@ssga.ru\n630108, г. Новосибирск, ул. Плахотного 10,  каб. 228')

        elif HasString(message.text, "общага") or HasString(message.text, "общежитие") or HasString(message.text, "фото") or HasString(message.text, "новости") or HasString(message.text, "Прочее"):
            bot.send_message(message.chat.id, 'Всю остальную информацию, как фотографии нашего университета или нашего общежития; новости в различных сферах (наука, спорт или даже киберспорт); расписание и другое, можно найти на главном сайте СГУГиТ.\nhttps://sgugit.ru/')
        else:
            bot.send_message(message.chat.id, 'Уточните свой вопрос.')

def HasString(data, s):
    a = data.lower()
    if a.find(s.lower()) != -1:
        return True
    else:
        return False