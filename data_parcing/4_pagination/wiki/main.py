import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    if r.ok: #200  ##403 404
        return r.text
    print(r.status_code)


def write_csv(list):
    with open('animals_list.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(list)


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    lis = soup.find('div', class_='mw-category-group').find_all('li')
    durty_list = []
    for li in lis:
        try:
            name = li.find('a').text
        except:
            name = ''
        durty_list = [name]
        write_csv(durty_list)


def main():
    url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    while True:
        get_data(get_html(url))
        soup = BeautifulSoup(get_html(url), 'lxml')
        try:
            url = 'https://ru.wikipedia.org/' + soup.find('div', id='mw-pages').find_all('a')[-1].get('href')
        except:
            break


if __name__ == '__main__':
    main()
