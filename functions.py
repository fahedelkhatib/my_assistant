import os
import sys
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from io import BytesIO
from time import sleep
import pyglet

#for findWeather()
import python_weather
import asyncio


def speak(text):
    tts = gTTS(text=text, lang="en", tld='ie', slow=False) #sets language of speaker, text to be spoken
    filename = 'voice.mp3'
    tts.save(filename) #save tts audio to local file

    music = pyglet.media.load(filename, streaming=False) #play audio immediately
    music.play()

    sleep(music.duration)
    os.remove(filename) #delete local file

def get_audio():
    r = sr.Recognizer()
    #r.energy_threshold = 3000
    #r.pause_threshold = 0.5
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            #print("What you said: " + said)
            #os.system("del /f voice.mp3")
        except Exception as e:
            print("Exception: " + str(  e))
    return said
