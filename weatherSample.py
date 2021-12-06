# import the module
import python_weather
import asyncio

async def getweather():
    # declare the client. format defaults to the metric system (celcius, km/h, etc.)
    #client = python_weather.Client(format=python_weather.IMPERIAL)
    client = python_weather.Client()

    # fetch a weather forecast from a city
    weather = await client.find("Riverside California")

    # returns the current day's forecast temperature (int)
    print(weather.current.temperature)

    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)

    # close the wrapper once done
    await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())