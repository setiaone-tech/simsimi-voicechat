import speech_recognition as sr
import pyaudio
import requests
import json
import pyttsx3

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Do you want to say something?')
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        n = text
    except sr.UnknownValueError:
        print("Sepertinya bermasalah")
    except sr.RequestError as e:
        print("Cannot obtain result:{0}".format(e))

    headers = {
        'Content-Type': 'application/json',
        'x-api-key': 'ArZm9yIfeK4~LkS0-iviV-65pDrO7e3gy9dn_DNP',
    }

    url = 'https://wsapi.simsimi.com/190410/talk/'
    body = {
        'utext': n, 
        'lang': 'en',
        'country': ['US'],
        'atext_bad_prob_max': '0.7'
    }

    response = requests.post("https://wsapi.simsimi.com/190410/talk/", data=json.dumps(body), headers=headers)
    pp = response.json()
    tt = pp.get("atext")

    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(tt)
    engine.runAndWait()