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

def print_readout():
    print("readout printed")

async def findWeather():
    client = python_weather.Client()
    weather = await client.find("Riverside California")
    print(weather.current.temperature)
    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)
    await client.close()
    curr = weather.current
    return curr.temperature, curr.sky_text

def eToEy(inputString):
    inputString = inputString.casefold()
    if(inputString[-1] == ('e')):
        inputString, pop = inputString[:-1], inputString[-1] #split into two arrays, save part without ommitted contents
        inputString= inputString + "ey"
    return inputString


speak("speak into the microphone now")
spokenWords = get_audio().encode('ascii', 'ignore')

print(b'You said: ' + spokenWords)
#speak(b'You said:' + spokenWords)

if(spokenWords == b'read results'):
    print_readout()

if(spokenWords == b'tell me the weather'):
    loop = asyncio.get_event_loop()
    temperature, skyCondition = loop.run_until_complete(findWeather())
    #add precipitation, wind speed, sky condition
    
    #process string for good grammar
    skyCondition = eToEy(skyCondition)
    speak("The temperature in Corona California is " + str(temperature) + " degrees celcius." + "Skies are " + str(skyCondition))