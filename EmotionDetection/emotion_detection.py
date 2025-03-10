import requests
import json


def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    jsonObject = {"raw_document": {"text": text_to_analyse}}

    res = requests.post(url, json=jsonObject, headers=header)

    if (res.status_code == 400):
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    else:
        json_response = json.loads(res.text)
        predictions = json_response["emotionPredictions"][0]["emotion"]

        anger_score = predictions["anger"]
        disgust_score = predictions["disgust"]
        fear_score = predictions["fear"]
        joy_score = predictions["joy"]
        sadness_score = predictions["sadness"]

        formatted_response = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
        }

        dominant_emotion = max(formatted_response, key=formatted_response.get)
        formatted_response["dominant_emotion"] = dominant_emotion

        return formatted_response
