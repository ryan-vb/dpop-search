from bs4 import BeautifulSoup
from selenium import webdriver

from scrape import scrape
from parse import dpop_listings


if __name__ == "__main__":
    driver = webdriver.Chrome()
    page_html = scrape.dpop_search(driver, "#eyeshadow")
    page_soup = BeautifulSoup(page_html)
    price_range = dpop_listings.get_prices(page_soup)

    print("min: " + price_range["min"])
    print("mean: " + price_range["mean"])
    print("max: " + price_range["max"])
