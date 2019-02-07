from source import *
import pprint


class aldiScraper(shopScraper):

    def __init__(self, url):
        shopScraper.__init__(self, url)
        self.url = self.url + self.findHref()
        print(self.url)

        self.dict = {"categories": {}}

    def findHref(self): #btn btn--primary btn--block
        try:
            html = urlopen(self.url)

        except HTTPError as e:
            return None
        try:
            bs = BeautifulSoup(html.read(), 'html.parser')
            newUrl = bs.body.find('a', {'class': 'btn btn--primary btn--block'}, href=True)
            newUrl = newUrl['href']

        except AttributeError as e:
            return None

        return newUrl
