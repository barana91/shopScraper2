from source import *
import pprint

from babel.numbers import parse_decimal, parse_number


class reweScraper(shopScraper):

    def __init__(self, url):
        shopScraper.__init__(self, url)

        self.dict = {"categories": {}}
        print(self.url)

    def getBody(self, text=True):
        try:
            html = urlopen(self.url)

        except HTTPError as e:
            return None
        try:
            bs = BeautifulSoup(html.read(), 'html.parser')
            info = bs.body.findAll('div', {'class': 'card-body'})

        except AttributeError as e:
            return None
        return self.printer(info, text)

    def infoSibLev0(self, text=True):

        try:
            html = urlopen(self.url)

        except HTTPError as e:
            return None
        try:
            bs = BeautifulSoup(html.read(), 'html.parser')
            sib = bs.find('div',
                          {'class': 'row half-gutters mb-3 row-flex d-flex row-scroll-horizontal-xxs flex-xs-wrap'}).div
            title = bs.find('a', {'class': 'headline font-style-headline m-0 bg-white o-90'}).h2.get_text()
            self.dict["categories"] = {title: {}}
        except AttributeError as e:
            return None

        product_name = sib.div.find('p', {'class': 'headline font-style-body-2 py-2 mb-0'}).span.get_text()
        product_price = parse_decimal(sib.div.find('div', {'class': 'price-euro'}).get_text() + sib.div.find('div', {
            'class': 'price-cent'}).get_text())
        self.dict["categories"][title][0] = {'product': product_name, 'price': product_price}
        for idx, sibling in enumerate(sib.next_siblings):
            product_name = sibling.div.find('p', {'class': 'headline font-style-body-2 py-2 mb-0'}).span.get_text()
            product_price = parse_decimal(
                sibling.div.find('div', {'class': 'price-euro'}).get_text() + sibling.div.find('div', {
                    'class': 'price-cent'}).get_text())
            print(product_name, product_price)
            self.dict["categories"][title][idx + 1] = {'product': product_name, 'price': product_price}

        print(self.dict)

    def getShoppingCart(self):

        try:
            html = urlopen(self.url)

        except HTTPError as e:
            return None
        try:
            bs = BeautifulSoup(html.read(), 'html.parser')
            sib = bs.find('div', {'class': 'container'})
            sib1 = sib.find('div', {'class': 'drm-overview mb-3'}).div
            # print(sib1.prettify())

            # sib = bs.find('div', {'class': 'drm-overview mb-3'})

        except AttributeError as e:
            return None

        categories = sib1.div['id']
        self.dict["categories"][0] = {categories: {}}
        for idx, sibling0 in enumerate(sib1.next_siblings):
            self.dict["categories"][idx + 1] = {sibling0.div['id']: {}}

        sib2 = sib1.div.findAll('div', {'class': 'card-body'})
        first_cat = list(self.dict["categories"][0].keys())[0]

        for idx, sibling0 in enumerate(sib2):
            product_name = sibling0.find('p', {'class': 'headline font-style-body-2 py-2 mb-0'}).span.get_text()
            product_price = parse_decimal(
                sibling0.div.find('div', {'class': 'price-euro'}).get_text() + sibling0.div.find('div', {
                    'class': 'price-cent'}).get_text())

            self.dict["categories"][0][first_cat][idx + 1] = {"product_name": product_name, "price": product_price}

        for idx1, sibling0 in enumerate(sib1.next_siblings):

            sib3 = sibling0.div.findAll('div', {'class': 'card-body'})

            for idx2, sibling1 in enumerate(sib3):
                product_name = sibling1.find('p', {'class': 'headline font-style-body-2 py-2 mb-0'}).span.get_text()
                product_price = parse_decimal(
                    sibling1.div.find('div', {'class': 'price-euro'}).get_text() + sibling1.div.find('div', {
                        'class': 'price-cent'}).get_text())
                self.dict["categories"][idx1 + 1][list(self.dict["categories"][idx1 + 1].keys())[0]][idx2 + 1] = {
                    "product_name": product_name, "price": product_price}

        pp = pprint.PrettyPrinter(width=41, compact=True)
        pp.pprint(self.dict)
        return self.dict

    def getProductInfoLev1(self, text=True):
        try:
            html = urlopen(self.url)

        except HTTPError as e:
            return None
        try:
            bs = BeautifulSoup(html.read(), 'html.parser')
            info = bs.find('div', {'class': 'card drm-item-card h-100'})

        except AttributeError as e:
            return None
        return self.printerOne(info, text)

    # kann raus
    @staticmethod
    def printerOne(info, text=True):

        if (text == True):

            print(" ", info.get_text())
        else:
            print(info.prettify())

    # kann raus
    @staticmethod
    def printerAll(info, text=True):

        for name in info:
            if (text == True):
                print(" ", name.get_text())
            else:
                print(name.prettify())
