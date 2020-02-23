import configparser
from weather.weather import Weather


def get_key(section, key):
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config[section][key]

def main():
    my_weather = Weather(get_key('openweathermap', 'api'), get_key('openweathermap', 'location'))

    weather = my_weather.get_weather()
    forecast = my_weather.get_forecast()

    print("Weather:")
    print(weather['main']['temp'])
    print(weather)

    print("")
    print("Forecast:")
    print(forecast)

if __name__ == '__main__':
    main()