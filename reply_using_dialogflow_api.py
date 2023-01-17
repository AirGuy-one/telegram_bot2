from google.cloud import dialogflow


def reply_using_dialogflow_api(message, dialogflow_project_id, user_tg_chat_id):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(
        dialogflow_project_id,
        user_tg_chat_id
    )

    text_input = dialogflow.TextInput(text=message, language_code='en-US')

    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    return response
