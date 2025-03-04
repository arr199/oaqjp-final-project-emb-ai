"""
Emotion Detector Flask Application

This application provides a REST API endpoint that detects emotions in text
using the EmotionDetection module. It returns emotion scores and the dominant emotion.
"""
from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector App")


@app.route("/emotionDetector")
def get_emotions():
    """ 
     Endpoint to detect emotions in text.
    """
    text_to_analyse = request.args.get("textToAnalyse")

    formatted_response = emotion_detector(text_to_analyse)

    if formatted_response["dominant_emotion"] is None:
        return "Invalid text! Please try again!."

    text_response = (
        f"For the given statement, the system response is 'anger': {formatted_response['anger']}, "
        f"'disgust': {formatted_response['disgust']}, "
        f"'fear': {formatted_response['fear']}, "
        f"'joy': {formatted_response['joy']}, "
        f"and 'sadness': {formatted_response['sadness']}. "
        f"The dominant emotion is {formatted_response['dominant_emotion']}."
    )
    return text_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
