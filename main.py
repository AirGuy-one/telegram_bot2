from dotenv import load_dotenv
from telebot import types
from google.cloud import dialogflow
from create_intent_using_json import create_intent_using_json

import telebot
import os


load_dotenv()

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
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(
        os.environ['DIALOG_FLOW_PROJECT_ID'],
        os.environ['USER_TG_CHAT_ID']
    )

    text_input = dialogflow.TextInput(text=message.text, language_code='en-US')

    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    bot.send_message(message.chat.id, response.query_result.fulfillment_text)


if __name__ == '__main__':
    if input('Do you wanna create an intent?(y/n)\n') == 'y':
        create_intent_using_json('phrases.json')

    bot.infinity_polling()
