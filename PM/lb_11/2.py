import requests


url = 'http://geocode-maps.yandex.ru/1.x/'
params = {'apikey': '8013b162-6b42-4997-9691-77b7074026e0',
          'geocode': input('Адрес: '),
          'format': 'json'}

response = requests.get(url, params)
if response:
    data = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
    postal_code = data['metaDataProperty']['GeocoderMetaData']['Address']['postal_code']
    if postal_code:
        print(postal_code)
    else:
        print('Почтовый индекс не найден')
