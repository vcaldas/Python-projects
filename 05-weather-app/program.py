import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport', 'condition, temp, scale, location')


def cleanup_text(text: str):
    if not text:
        return text
    else:
        text = text.strip()

        return text


def find_city_and_state(location):
    parts = location.split('\n')
    return parts[0].strip()



def get_weather_from_html(html):
#    cityCss = '.region-content-header h1'
#    weather_scale_css = '.wu-unit-temperature .wu-label'
#    weather_temp_csvv = '.wu-unit-temperature .wu-value'
#    weaher_condition_css = 'condition-icon'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    location = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    location = cleanup_text(location)
    location = find_city_and_state(location)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    report = WeatherReport(condition=condition, location=location, temp=temp, scale=scale)

    return report



def main():
    print_header()
    zip_code = input ('What is your zipcode? ex. 97201')
    html = get_html_from_web (zip_code)

    report = get_weather_from_html(html)


    print('The weather ir {} is {}. Temperature: {} {}'.format(report.location, report.condition, report.temp, report.scale))
    print('Done!')


def get_zipcode():
    zip_code = input('Type the zipcode (ex. 97201): ')

    return zip_code


def get_html_from_web(zip_code):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zip_code)
    response = requests.get(url)

    return response.text

def print_header():
    print('------------------')
    print('   Weather App')
    print('------------------')
    print()


if __name__ == '__main__':
    main()

