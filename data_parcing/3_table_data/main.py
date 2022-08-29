'''Parsing table data using the example of a Cryptocurrency exchange website '''

import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text 


def write_csv(data):
    with open('cmc.csv', 'a', encoding='utf-8') as f: 
        writer = csv.writer(f)

        writer.writerow((data['name'],
                         data['volume'],
                         data['url']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table').find('tbody').find_all('tr')
    
    for tr in trs:
        tds1 = tr.find_all('a', class_='cmc-link')
        ps = tds1[0].find_all('p')
        name = ps[0].get_text()
        url = 'https://coinmarketcap.com' + tr.find('a', class_='cmc-link').get('href')
        volume = tds1[1].find('p').get_text()
        data = {'name': name,
                'volume': volume,
                'url': url,
                }
        
        write_csv(data)
        
        

def main():
    url = 'https://coinmarketcap.com/ru/rankings/exchanges/'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
