from statistics import mean, mode

from bs4 import BeautifulSoup


class DpopParser:
    def __init__(self, soup):
        if isinstance(soup, BeautifulSoup):
            self.soup = soup
        elif isinstance(soup, str):
            self.soup = BeautifulSoup(soup, features="html.parser")

    def get_prices(self):
        prices_elements = self.soup.find_all(attrs={"aria-label": "Price"})

        return list(map(lambda x: float(x.text[2:]), prices_elements))

    def get_links(self):
        prices_elements = self.soup.find_all(
            attrs={"class": "styles__ProductCard-sc-5cfswk-2"})

        return list(map(lambda x: x.attrs["href"], prices_elements))

    def get_listing_description(self):
        return str(self.soup.find(attrs={"class": "styles__DescriptionContainer-uwktmu-9"}))

    @staticmethod
    def get_stats(values: list):
        price_min = min(values)
        price_max = max(values)
        price_mean = mean(values)
        price_mode = mode(values)

        return {'max': price_max, 'min': price_min, 'mean': price_mean, 'mode': price_mode}
