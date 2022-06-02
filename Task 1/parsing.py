# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

words = []
url = 'http://sherwoodschool.ru/vocabulary/upperintermediate/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('a', target='_blank')

for quote in quotes:
    if 'fianc' not in quote.text and 'Foxinet' not in quote.text:
        words.append(quote.text.lower())
    else:
        pass
with open('words.txt', 'w') as f1, open('words.txt', 'r') as f2:
    if f2.read() == '':
        for i in words:
            if i != '':
                f1.write(i + '\n')
    else:
        pass
