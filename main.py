# https://www.agiratech.com/web-scraping-using-python/
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

urls = ['https://www.example.com/products/mobiles-mobile-phones?sort=plrty',
        'https://yandex.ru/',
        ]

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'
    'AppleWebKit/537.36 (KHTML, like Gecko)'
    'Chrome/64.0.3282.167 Safari/537.36'
    }


def get_result_from_url(url, headers):
    return requests.get(url, headers=headers, verify=True)


def get_soup_from_result(result):
    soup = BeautifulSoup(result.content, 'html.parser')
    return soup


if __name__ == '__main__':
    result = get_result_from_url(urls[1], headers)
    print(result)
