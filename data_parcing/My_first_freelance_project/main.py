import requests
from bs4 import BeautifulSoup



def get_html(url):
    html_pack = requests.get(url)
    return html_pack.text


def write_txt(data):
    with open('beer.txt', 'a', encoding='utf-8') as f:
        f.write(data + '\n')


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    lots = soup.find_all('div', class_='item_block col-4')
    for lot in lots:
        pivo = lot.find('div', class_='item-title').find('span').text
        write_txt(pivo)


def main():
    url = 'https://rus-beer.ru/catalog/razlivnoe_pivo/'
    for i in range(2, 9):
        (get_data(get_html(url)))
        url = f"https://rus-beer.ru/catalog/razlivnoe_pivo/?PAGEN_1={i}"


if __name__ == '__main__':
    main()