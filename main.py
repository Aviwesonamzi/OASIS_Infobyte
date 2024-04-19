import speech_recognition as sr
import pywhatkit
from gtts import gTTS
import playsound
import os
import time

#making the program say something to us
def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
speak("Hello everybody")
#getting audio from the user
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recogniz_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said

text = get_audio()
