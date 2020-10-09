from bs4 import BeautifulSoup
from selenium import webdriver

from . import scrape
from . import parse


if __name__ == "__main__":
    driver = webdriver.Chrome()
    page_html = scrape.dpop_search(driver, "main squeeze eyeshadow palette")
    page_soup = BeautifulSoup(page_html)
    price_range = parse.get_price_range(page_soup)

    print("min: " + price_range["min"])
    print("mean: " + price_range["mean"])
    print("max: " + price_range["max"])
