#!/usr/bin/env python3

import urllib.request
import csv

from bs4 import BeautifulSoup
def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


URLurrl = 'http://absurdopedia.net/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B4%D0%BE%D1%80%D0%BE%D0%B6%D0%BD%D1%8B%D1%85_%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%B2,_%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D0%B5%D0%BC%D1%8B%D1%85_%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8'


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='wikitable')

    roadsigns = []

    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        try:
            roadsigns.append({
                'number': cols[0].text,
                'title': cols[2].text,
                'description': cols[3].text
            })
        except:
            print('ERR:', cols)

    return roadsigns

def save(roadsigns, path):
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Номер', 'Название', 'Описание'))

        for test1 in roadsigns:
            writer.writerow((test1['number'], test1['title'], test1['description']))

def main():
    roadsigns = []
    parse(get_html(URLurrl))
    save(roadsigns, 'roadsigns.csv')

if __name__ == '__main__':
    main()