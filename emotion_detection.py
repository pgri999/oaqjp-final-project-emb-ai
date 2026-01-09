import requests
import json

#function to run emotion detection
def emotion_detector(text_to_analyze):

    #preparing url, header and json object to send
    url = (
        'https://sn-watson-emotion.labs.skills.network/'
    'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {"grpc-metadata-mm-model-id":
    "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    #sending the request
    response = requests.post(url, json = myobj, headers=headers)

    #converting the request in json
    formatted_response=json.loads(response.text)

    #extracting only the emotions from the response
    dico=formatted_response["emotionPredictions"][0]
    emotions = dico['emotion']

    # Find the key with the highest value
    dominant_key = max(emotions, key=emotions.get)

    # Add a new key 'dominant_emotion' to the dictionary
    emotions['dominant_emotion'] = dominant_key

    return emotions
