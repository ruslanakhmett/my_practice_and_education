import requests
from bs4 import BeautifulSoup
import csv



def get_html(url):
    user_agent =  {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    r = requests.get(url, headers=user_agent)
    return r.text


def write_csv(data):
    with open('testimonials.csv', 'a') as f:
        order = ['author', 'since']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)


def get_articles(html):
    soup = BeautifulSoup(html, 'lxml')
    ts = soup.find('div', class_='testimonial-container').find_all('article')
    return ts


def get_page_data(ts):
    for t in ts:
        try:
            since = t.find('p', class_='traxer-since').text.strip()
        except:
            since = ''
        try:
            author = t.find('p', class_='testimonial-author').text.strip()
        except:
            author = ''
        data = {'author': author, 'since': since}
        write_csv(data)


def main():
    while True:
        page = 1
        url = 'https://catertrax.com/why-catertrax/traxers/page/{}/?themify_builder_infinite_scroll=yes'.format(str(page))

        articles = get_articles(get_html(url))

        if articles:
            get_page_data(articles)
            page += 1
        else:
            break


if __name__ == '__main__':
    main()