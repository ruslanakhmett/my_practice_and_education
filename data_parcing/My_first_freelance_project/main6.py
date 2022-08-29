import requests
from bs4 import BeautifulSoup



def get_html(url):
    html_pack = requests.get(url)
    return html_pack.text


def write_txt(data):
    with open('styles.txt', 'a', encoding='utf-8') as f:
        f.write(data + '\n')


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    lots = soup.find_all('div', class_='item clearfix item_block')
    for lot in lots:
        pivo = lot.find('div', class_='item-title').find('span').text
        write_txt(pivo)


def main():
    url = 'https://rus-beer.ru/styles/'
    get_data(get_html(url))



if __name__ == '__main__':
    main()