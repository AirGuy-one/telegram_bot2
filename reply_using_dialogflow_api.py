from google.cloud import dialogflow

import os


def reply_using_dialogflow_api(message):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(
        os.environ['DIALOG_FLOW_PROJECT_ID'],
        os.environ['USER_TG_CHAT_ID']
    )

    text_input = dialogflow.TextInput(text=message, language_code='en-US')

    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    return response
