from vk_api.longpoll import VkLongPoll, VkEventType
from reply_using_dialogflow_api import reply_using_dialogflow_api
from dotenv import load_dotenv

import vk_api
import os
import telebot


def main():
    load_dotenv()

    vk_session = vk_api.VkApi(token=os.environ['VK_GROUP_TOKEN'])

    longpoll = VkLongPoll(vk_session)

    bot = telebot.TeleBot(
        os.environ.get('TG_BOT_TOKEN')
    )

    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                answer = event.text
                response = reply_using_dialogflow_api(
                    answer,
                    os.environ['DIALOG_FLOW_PROJECT_ID'],
                    os.environ['USER_TG_CHAT_ID']
                )

                if not response.query_result.intent.is_fallback:
                    answer = response.query_result.fulfillment_text

                    vk_session.method('messages.send', {
                        'user_id': event.user_id,
                        'message': answer,
                        'random_id': 0
                    })
    except Exception as e:
        bot.send_message(os.environ['USER_TG_CHAT_ID'], str(e))


if __name__ == '__main__':
    main()
