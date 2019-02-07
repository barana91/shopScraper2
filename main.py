from source.markets import reweScraper
from source.markets import aldiScraper

rewe = reweScraper('https://www.rewe.de/angebote/nationale-angebote')

#rewe.printAll()
rewe.getShoppingCart()


#aldi = aldiScraper('https://www.aldi-nord.de').printAll()

#rewe.getProductInfoLev1(text=False)

