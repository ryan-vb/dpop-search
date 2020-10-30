from statistics import mean, mode

from bs4 import BeautifulSoup


def get_prices(soup: BeautifulSoup):
    prices_elements = soup.find_all(attrs={"aria-label": "Price"})

    return list(map(lambda x: float(x.text[2:]), prices_elements))


def get_links(soup: BeautifulSoup):
    prices_elements = soup.find_all(
        attrs={"class": "styles__ProductCard-sc-5cfswk-2"})

    return list(map(lambda x: x.attrs["href"], prices_elements))


def get_stats(values: list):
    price_min = min(values)
    price_max = max(values)
    price_mean = mean(values)
    price_mode = mode(values)

    return {'max': price_max, 'min': price_min, 'mean': price_mean, 'mode': price_mode}
