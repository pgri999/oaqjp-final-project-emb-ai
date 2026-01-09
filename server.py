''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Run Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector
        function. The output is a text summary of the info obtained
    '''
    #first we request the text to analyze
    text_to_analyze = request.args.get('textToAnalyze')

    #we run the emotion_detector
    answer_dic=emotion_detector(text_to_analyze)

    #we extract the keys and values of the answer (dictionnary)
    keys = list(answer_dic.keys())
    values = list(answer_dic.values())

    if values[5] is None:
        return '<b> Invalid text! Please try again!</b>'

    return (
        f"For the given statement, the system response is '{keys[0]}' : {values[0]}, '{keys[1]}': {values[1]}, "
        f"'{keys[2]}': {values[2]}, '{keys[3]}': {values[3]} and '{keys[4]}': {values[4]}. "
        f"The dominant emotion is <b>{values[5]}</b>."
    )

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port =5000)
