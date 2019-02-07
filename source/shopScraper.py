from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from types import *

'''
Main class for the shopScraper Application
'''
class shopScraper:

    def __init__(self, url):
        if not isinstance(url, str):
            raise TypeError('Not a URL')

        self.url = url

    def getTitle(self):
        try:
            html = urlopen(self.url)

        except HTTPError as e:
            return None
        try:
            bs = BeautifulSoup(html.read(), 'html.parser')
            title = bs.head.title
        except AttributeError as e:
            return None
        return print(title.get_text())

    def printAll(self):
        try:
            html = urlopen(self.url)

        except HTTPError as e:
            return None
        try:
            bs = BeautifulSoup(html.read(), 'html.parser')

        except AttributeError as e:
            return None
        return print(bs.body.prettify())








