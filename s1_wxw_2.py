import requests


def get_location():
    ipinfo = requests.get('https://ipinfo.io/json')
    return ipinfo.json()['city']


def get_weather(city):
    weather = requests.get(
        'https://api.apixu.com/v1/current.json?key=c780b28ca20d4426a25152234191002&q={}'.format(city))
    return weather.json()


def append_to_file(city, country, temp):
    with open('weather.txt', 'a') as file:
        file.write('The weather in {}, {} is {} degrees\n'.format(city, country, temp))

cities = ['Mumbai', 'Holon', 'London', 'New York', 'Tel Aviv', 'Eilat', 'Bangkok', 'Cairo', 'Paris', 'Melbourn']


if __name__ == '__main__':
    # city = get_location()
    for city in cities:
        weather = get_weather(city)
        country = weather['location']['country']
        temp = weather['current']['temp_c']
        append_to_file(city, country, temp)


