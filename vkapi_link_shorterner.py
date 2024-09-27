import requests
import os
from urllib.parse import urlparse
import argparse
from dotenv import load_dotenv

API_URL_SHORTEN_WITH_APIVK = 'https://api.vk.com/method/utils.getShortLink'
API_URL_STATS_WITH_APIVK = 'https://api.vk.com/method/utils.getLinkStats'
API_VERSION = '5.131'


def is_valid_url(url):
    parsed_url = urlparse(url)
    return parsed_url.scheme in ['http', 'https'] and parsed_url.netloc


def is_shortened_link(url):
    return urlparse(url).netloc == 'vk.cc'


def shorten_link(access_token, long_url):
    response = requests.get(API_URL_SHORTEN_WITH_APIVK, params={
        'access_token': access_token,
        'url': long_url,
        'v': API_VERSION
    })
    response.raise_for_status()
    return response.json()['response']['short_url']


def count_clicks(access_token, url_key):
    response = requests.get(API_URL_STATS_WITH_APIVK, params={
        'access_token': access_token,
        'key': url_key,
        'v': API_VERSION
    })
    response.raise_for_status()
    return response.json()['response'].get('clicks', 0)


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description='Сокращение ссылок.')
    parser.add_argument('long_url', type=str,
                        help='Длинная ссылка')

    args = parser.parse_args()


    vk_token = os.environ['VK_TOKEN']

    if not is_valid_url(args.long_url):
        print("Ошибка: некорректно введен адрес.")
        return

    if is_shortened_link(args.long_url):
        url_key = args.long_url.split('/')[-1]
        click_count = count_clicks(vk_token, url_key)
        print(f"Количество кликов по сокращенной ссылке: {click_count}")
    else:
        shortened_url = shorten_link(vk_token, args.long_url)
        print(f"Сокращенная ссылка: {shortened_url}")


if __name__ == '__main__':
    main()
