import requests


apikey = '78a45f73ed1310f62dfa194797931fa4'
city = 'Москва'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units=metric&lang=ru'
response = requests.get(url)
if response.status_code == 200:
    weather_data = response.json()
    temperature = weather_data['main']['temp']
    print(f"Температура в г.{city}: {temperature}°C")
else:
    print(f'Ошибка: {response.status_code}')
