from bs4 import BeautifulSoup
import rpa as r
from statistics import mean


def dpop_search(search_term):
    r.init()
    r.url(f'https://www.depop.com/search')
    r.type('//*[@name="q"]', f'{search_term}[enter]')
    print(r.read('result-stats'))
    r.snap('page', 'results.png')
    page_text = r.text()
    r.close()

    return BeautifulSoup(page_text)


def get_pricerange(soup: BeautifulSoup):
    prices_elements = soup.find_all("span", attrs={"aria-lable": "Price"})

    price_float = map(lambda x: float(x[1:]), prices_elements)

    price_min = min(price_float)
    price_max = max(price_float)
    price_mean = mean(price_float)

    return {'max': price_max, 'min': price_min, 'mean': price_mean}

