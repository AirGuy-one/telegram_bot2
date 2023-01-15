from dotenv import load_dotenv
from telebot import types
from google.cloud import dialogflow
from google_dialogflow_api import google_dialogflow_api

import telebot
import os


load_dotenv()

bot = telebot.TeleBot(
    os.environ.get('TG_BOT_TOKEN')
)


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    greet_button = types.KeyboardButton('👋 Greet')
    markup.add(greet_button)
    bot.send_message(message.from_user.id, 'Hello', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def repeat_our_message(message):
    response = google_dialogflow_api(message.text)

    bot.send_message(message.chat.id, response.query_result.fulfillment_text)


def launch_tg_bot():
    try:
        bot.infinity_polling()
    except Exception as e:
        bot.send_message(os.environ['USER_TG_CHAT_ID'], str(e))
