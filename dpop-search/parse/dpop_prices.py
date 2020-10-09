from statistics import mean, mode

from bs4 import BeautifulSoup


def get_price_range(soup: BeautifulSoup):
    prices_elements = soup.find_all(attrs={"aria-label": "Price"})

    return list(map(lambda x: float(x.text[2:]), prices_elements))


def get_stats(values: list):
    price_min = min(values)
    price_max = max(values)
    price_mean = mean(values)
    price_mode = mode(values)

    return {'max': price_max, 'min': price_min, 'mean': price_mean, 'mode': price_mode}


if __name__ == '__main__':
    with open("test.html", "r") as f:
        html = f.read()
    soup = BeautifulSoup(html)
    values = get_price_range(soup)
    results = get_stats(values)
    print(results["min"])
    print(results["mean"])
    print(results["mode"])
    print(results["max"])


