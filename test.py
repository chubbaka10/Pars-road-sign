#!/usr/bin/env python3

import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
	response = urllib.request.urlopen(url)
	return response.read()

def parse(html):

	soup = BeautifulSoup(html, 'html.parser')
	table = soup.find('table', class_='tviz')
	rows = table.find_all('tr')[0:]

	
	print(rows)

def main():
	parse(get_html('http://www.50kopeekvrn.ru/index.php/dorozhnye-znaki/perechen-dorozhnykh-znakov/'))

if __name__ == '__main__':
	main()
