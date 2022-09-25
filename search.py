import requests
from pyfiglet import Figlet
import folium


def get_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        # print(response)
        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('cite'),
            '[Zip]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }
        for k, v in data.items():
            print(f'{k} : {v}')
        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")} {response.get("cite")}.html')
    except requests.exceptions.ConnectionError:
        print('[!] Please check you connection')


def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP INFO'))
    ip = input("Please enter a target ip: ")
    get_ip(ip=ip)


if __name__ == '__main__':
    main()
