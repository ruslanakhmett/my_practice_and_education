'''Parsing site elements(Plugins) and writing the results to a file '''
import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def refined(s):
    #1,868 total ratings
    r = s.split(' ')[0]
    return  r.replace(',', '')


def write_csv(data):
    with open('plugins.csv', 'a') as f:    #flag a - append, add data in file, no rewrite
        writer = csv.writer(f)

        writer.writerow((data['name'],
                         data['url'],
                         data['reviews'])) #make a tuple because for writerow ONE parameter is needed


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find_all('section')[3]
    plugins = popular.find_all('article') #4

    for plugin in plugins:
        name = plugin.find('h3').text #get plugins name
        url = plugin.find('h3').find('a').get('href') #get links for plugins
        
        r = plugin.find('span', class_='rating-count').find('a').text #get ratings
        rating = refined(r)

        data = {'name': name,
                'url': url,
                'reviews': rating }

        write_csv(data)    


def main():
    url = 'https://wordpress.org/plugins/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()