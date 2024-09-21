from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

#GET request to the HTML interface
@app.route("/emotionDetector")
def emo_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
   
    if dominant_emotion is None:
        return "Invalid input! Try again."
    else:
        # Return a formatted string with the emotion scores
        return "For the given statement, the system response is 'anger':{} , 'disgust':{} , 'fear':{} , 'joy':{} , 'sadness':{}. Name of the dominant emotion is {}.".format(anger, disgust, fear, joy, sadness, dominant_emotion)

#This function should simply run the render_template function on the HTML template
@app.route("/")
def render_index_page():
    return render_template('index.html')
#port number
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)