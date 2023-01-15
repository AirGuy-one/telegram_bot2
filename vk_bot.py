import vk_api
import os
import telebot

from vk_api.longpoll import VkLongPoll, VkEventType
from google.cloud import dialogflow
from google_dialogflow_api import google_dialogflow_api
from dotenv import load_dotenv

load_dotenv()

vk_session = vk_api.VkApi(token=os.environ['VK_GROUP_TOKEN'])

longpoll = VkLongPoll(vk_session)

bot = telebot.TeleBot(
    os.environ.get('TG_BOT_TOKEN')
)


def launch_vk_bot():
    try:
        for event in longpoll.listen():
            global answer
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    answer = event.text
                    if event.from_user:
                        response = google_dialogflow_api(answer)

                        if not response.query_result.intent.is_fallback:
                            answer = response.query_result.fulfillment_text

                            vk_session.method('messages.send', {
                                'user_id': event.user_id,
                                'message': answer,
                                'random_id': 0
                            })
    except Exception as e:
        bot.send_message(os.environ['USER_TG_CHAT_ID'], str(e))
