import requests

def weather_api(city):
    api_key = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a909d755ac989d92a76142650a8099b1&units=metric"
    try:
        responce= requests.get(api_key)
        responce.raise_for_status()
        data = responce.json()
        print(data['main']['temp'])
        print(data['weather'][0]['description'])
        print(data['name'])
        print(data['sys']['country'])
        
    except requests.exceptions.RequestException as e:
        print(e)

city= input("enter the name")
weather_api(city)