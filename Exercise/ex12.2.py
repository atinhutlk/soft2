import os
import requests

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature_kelvin = data['main']['temp']
            temperature_celsius = kelvin_to_celsius(temperature_kelvin)

            return f"Weather in {city}: {weather_description}, Temperature: {temperature_celsius:.2f}°C"
        else:
            return f"Failed to fetch weather information. Error: {data['message']}"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    api_key = "ce08ad94ffe4b2d5adda00309a48133b"

    city = input("Enter the name of a municipality: ")
    result = get_weather(api_key, city)
    print(result)
