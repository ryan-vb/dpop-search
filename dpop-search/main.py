from bs4 import BeautifulSoup
# import rpa as r

from statistics import mean




def get_price_range(soup: BeautifulSoup):
    prices_elements = soup.find_all(attrs={"aria-label": "Price"})

    price_float = list(map(lambda x: float(x.text[1:]), prices_elements))

    price_min = min(price_float)
    price_max = max(price_float)
    price_mean = mean(price_float)

    return {'max': price_max, 'min': price_min, 'mean': price_mean}


if __name__ == "__main__":
    driver = webdriver.Chrome()
    page_html = dpop_search(driver, "main squeeze eyeshadow palette")
    driver.close()

    page_soup = BeautifulSoup(page_html)
    price_range = get_price_range(page_soup)

    print("min: " + price_range["min"])
    print("mean: " + price_range["mean"])
    print("max: " + price_range["max"])
