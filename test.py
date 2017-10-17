#!/usr/bin/env python3

import urllib.request

from bs4 import BeautifulSoup
def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='wikitable')

    roadsigns = []

    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        try:
            roadsigns.append({
                'title': cols[2].text,
                'wall': cols[3].text
            })
        except:
            print('ERR:', cols)

    for test1 in roadsigns:
        print(test1)

def main():
    parse(get_html('http://absurdopedia.net/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B4%D0%BE%D1%80%D0%BE%D0%B6%D0%BD%D1%8B%D1%85_%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%B2,_%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D0%B5%D0%BC%D1%8B%D1%85_%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8'))


print(main())