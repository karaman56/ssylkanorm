import requests
import os
from urllib.parse import urlparse

API_URL_SHORTEN_WITH_APIVK = 'https://api.vk.com/method/utils.getShortLink'
API_URL_STATS_WITH_APIVK = 'https://api.vk.com/method/utils.getLinkStats'
API_VERSION = '5.131'


def is_valid_url(url):
    parsed_url = urlparse(url)
    return all([parsed_url.scheme in ['http', 'https'], parsed_url.netloc])


def is_shortened_link(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc == 'vk.cc'


def shorten_link(access_token, long_url):
    params = {
        'access_token': access_token,
        'url': long_url,
        'v': API_VERSION
    }
    response = requests.get(API_URL_SHORTEN_WITH_APIVK, params=params)
    response.raise_for_status()
    return response.json()['response']['short_url']


def count_clicks(access_token, url_key):
    params = {
        'access_token': access_token,
        'key': url_key,
        'v': API_VERSION
    }
    response = requests.get(API_URL_STATS_WITH_APIVK, params=params)
    response.raise_for_status()
    return response.json()['response'].get('clicks', 0)


def main():
    long_url_input = input("Введите ссылку: ")
    VK_API_TOKEN = os.environ.get('vk_token')
    if not is_valid_url(long_url_input):
        print("Ошибка: введен некорректный адрес.")
        return

    try:
        if is_shortened_link(long_url_input):
            url_key = long_url_input.split('/')[-1]
            click_count = count_clicks(VK_API_TOKEN, url_key)
            print(f"Количество кликов по сокращенной ссылке: {click_count}")
        else:
            shortened_url = shorten_link(VK_API_TOKEN, long_url_input)
            print(f"Сокращенная ссылка: {shortened_url}")
    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при запросе: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    main()


