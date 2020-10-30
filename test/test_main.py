import unittest

from dpop_search.parse import dpop_listings


class TestGetPrices(unittest.TestCase):
    def setUp(self):
        with open("test/test_data/test.html", "r") as f:
            html = f.read()
        self.soup = dpop_listings.BeautifulSoup(html, "html.parser")

    def test_get_prices(self):
        values = dpop_listings.get_prices(self.soup)
        self.assertEqual(values,
                         [19.99, 14.0, 20.0, 20.0, 18.0, 20.0, 20.0, 20.0, 12.0])

    def test_get_links(self):
        values = dpop_listings.get_links(self.soup)
        self.assertEqual(values, ['/products/fludey-colourpop-main-squeeze-eyeshadow-palette/',
                                  '/products/morandawsonkiki-colourpop-main-squeeze-eyeshadow/',
                                  '/products/sa_ara-colourpop-main-squeeze-/',
                                  '/products/laylamayla25-colourpop-main-squeeze-9-shade/',
                                  '/products/jar736-coming-soon-colourpop-87c5/',
                                  '/products/sa_ara-colourpop-miss-bliss-/',
                                  '/products/sa_ara-colourpop-its-my-pleasure/',
                                  '/products/sa_ara-colourpop-blue-moon-/',
                                  '/products/isabelle_rose-kylie-jenner-kylie-cosmetics-2/'])


class TestGetStats(unittest.TestCase):

    def setUp(self):
        values = [0, 2, 4, 6]
        self.results = dpop_listings.get_stats(values)

    def test_get_stats_min(self):
        self.assertEqual(self.results["min"], 0)

    def test_get_stats_mean(self):
        self.assertEqual(self.results["mean"], 3)

    def test_get_stats_mode(self):
        self.assertEqual(self.results["mode"], 0)

    def test_get_stats_max(self):
        self.assertEqual(self.results["max"], 6)


if __name__ == '__main__':
    unittest.main()
