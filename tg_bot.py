from telebot import types
from google.cloud import dialogflow
from google_dialogflow_api import google_dialogflow_api

import telebot
import os


bot = telebot.TeleBot(
    os.environ.get('TG_BOT_TOKEN')
)


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('👋 Поздороваться')
    markup.add(btn1)
    bot.send_message(message.from_user.id, 'Здравствуйте', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def repeat_our_message(message):
    response = google_dialogflow_api(message.text)

    bot.send_message(message.chat.id, response.query_result.fulfillment_text)


def launch_tg_bot():
    # If you want to create an intent, uncomment following two rows of code
    # from create_intent_using_json import create_intent_using_json
    # create_intent_using_json('phrases.json')
    try:
        bot.infinity_polling()
    except Exception as e:
        bot.send_message(os.environ['USER_TG_CHAT_ID'], str(e))
