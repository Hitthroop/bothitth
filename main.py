import telebot
import config


from tBot import tCommands
from tBot import tInPoint
from tBot import tCallback

bot = telebot.TeleBot(config.TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
    tCommands.Start(bot, message)


@bot.message_handler(content_types=['text'])
def dialog(message):
    tInPoint.ReadText(bot, message)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    tCallback.CallbackMsg(call, bot)


# RUN
bot.polling(none_stop=True)