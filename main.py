import functions


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