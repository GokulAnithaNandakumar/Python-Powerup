import pyttsx3
import requests

jarvis = pyttsx3.init()
jarvis.setProperty("rate", 180)
jarvis.setProperty("volume", 0.5)

voices = jarvis.getProperty("voices")
jarvis.setProperty("voice", voices[1].id)

CITY_NAME = "Vellore"
API_KEY = "682a2c96e35a41e5aa3175411242203"

def main():
    # jarvis.say("Hello, How are you doing today? I am here to tell you the weather of your city. What is your city?")
    # jarvis.runAndWait()
    
    CITY_NAME = input("Enter your city: ")
    BASE_URL = f"http://api.weatherapi.com/v1/current.json?key=682a2c96e35a41e5aa3175411242203&q={CITY_NAME}&aqi=no"
    
    # jarvis.say("Please wait for a moment. I am fetching the data.")
    # jarvis.runAndWait()
    
    response = requests.get(BASE_URL).json()
    string = response
    print(string)

    # {'location': {'name': 'Vellore', 'region': 'Tamil Nadu', 'country': 'India', 'lat': 12.93, 'lon': 79.13, 'tz_id': 'Asia/Kolkata', 'localtime_epoch': 1711166503, 'localtime': '2024-03-23 9:31'}, 'current': {'last_updated_epoch': 1711166400, 'last_updated': '2024-03-23 09:30', 'temp_c': 29.4, 'temp_f': 84.9, 'is_day': 1, 'condition': {'text': 'Sunny', 'icon': '//cdn.weatherapi.com/weather/64x64/day/113.png', 'code': 1000}, 'wind_mph': 4.9, 'wind_kph': 7.9, 'wind_degree': 161, 'wind_dir': 'SSE', 'pressure_mb': 1013.0, 'pressure_in': 29.9, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 45, 'cloud': 0, 'feelslike_c': 30.0, 'feelslike_f': 86.1, 'vis_km': 10.0, 'vis_miles': 6.0, 'uv': 7.0, 'gust_mph': 5.7, 'gust_kph': 9.1}}
    
    temperature = string['current']['temp_c']
    description = string['current']['condition']['text']
    humidity = string['current']['humidity']
    
    jarvis.say(f"The temperature in {CITY_NAME} is {temperature} degree celsius. The weather is {description}. The humidity is {humidity} percent.")
    
if __name__ == "__main__":
    main()