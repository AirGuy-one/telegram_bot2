from google.cloud import dialogflow

import json
import os


def create_intent(project_id, display_name, training_phrases_parts, message_texts):

    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )


def create_intent_using_json(phrases_file):
    with open(phrases_file) as phrases_file:
        phrases = json.load(phrases_file)

    for display_name, phrase in phrases.items():
        create_intent(
            os.environ['DIALOG_FLOW_PROJECT_ID'],
            display_name,
            phrase['questions'],
            [phrase['answer']]
        )
