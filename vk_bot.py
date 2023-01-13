import vk_api
import os
import telebot

from vk_api.longpoll import VkLongPoll, VkEventType
from google.cloud import dialogflow
from dotenv import load_dotenv

load_dotenv()

vk_session = vk_api.VkApi(token=os.environ['VK_GROUP_TOKEN'])

longpoll = VkLongPoll(vk_session)

bot = telebot.TeleBot(
    os.environ.get('TG_BOT_TOKEN')
)


def vk_bot_start():
    try:
        for event in longpoll.listen():
            global answer
            if event.type == VkEventType.MESSAGE_NEW:
                print('Новое сообщение:')
                if event.to_me:
                    print('Для меня от: ', event.user_id)
                    answer = event.text
                    print('Текст:', answer)
                    if event.from_user:
                        session_client = dialogflow.SessionsClient()
                        session = session_client.session_path(
                            os.environ['DIALOG_FLOW_PROJECT_ID'],
                            '123456789',
                        )
                        text_input = dialogflow.TextInput(text=answer, language_code='en-US')
                        query_input = dialogflow.QueryInput(text=text_input)
                        response = session_client.detect_intent(
                            request={"session": session, "query_input": query_input}
                        )

                        if not response.query_result.intent.is_fallback:
                            answer = response.query_result.fulfillment_text

                            vk_session.method('messages.send', {
                                'user_id': event.user_id,
                                'message': answer,
                                'random_id': 0
                            })
                else:
                    print('От меня для: ', event.user_id)
                    print('Текст:', answer)
    except Exception as e:
        bot.send_message(os.environ['USER_TG_CHAT_ID'], str(e))
