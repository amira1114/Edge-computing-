#!/usr/bin/env python
# coding: utf-8

from flask import Flask,render_template,url_for,request
import speech_recognition as sr

#from random import randint

app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/speechtotext',methods=['POST'])

def index():
    if request.method == "POST":
        recognizer = sr.Recognizer()
        mic  = sr.Microphone()
        with mic as source:
            sr.energy_threshold = 4000
            audio_data = recognizer.record(source, duration = 5)
    my_text = recognizer.recognize_google(audio_data)
    #my_text = "HELLO: %d" % randint(100, 999) 
    return render_template('result.html',text = my_text)


if __name__ == '__main__':
    app.run(debug=True)
