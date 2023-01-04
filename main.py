from dotenv import load_dotenv
from telebot import types

import telebot
import os


load_dotenv()

bot = telebot.TeleBot(
    os.environ.get('BOT_TOKEN')
)


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def repeat_our_message(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.infinity_polling()
