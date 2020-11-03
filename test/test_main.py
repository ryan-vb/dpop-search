import unittest

from dpop_search.parse.dpop_listings import DpopParser
from dpop_search.scrape.dpop_scrape import DpopScrape


class TestSearchPageParse(unittest.TestCase):
    def setUp(self):
        with open("test/test_data/test_search.html", "r") as f:
            html = f.read()
        self.parser = DpopParser(html)

    def test_get_prices(self):
        values = self.parser.get_prices()
        self.assertEqual(values,
                         [19.99, 14.0, 20.0, 20.0, 18.0, 20.0, 20.0, 20.0, 12.0])

    def test_get_links(self):
        values = self.parser.get_links()
        self.assertEqual(values, ['/products/fludey-colourpop-main-squeeze-eyeshadow-palette/',
                                  '/products/morandawsonkiki-colourpop-main-squeeze-eyeshadow/',
                                  '/products/sa_ara-colourpop-main-squeeze-/',
                                  '/products/laylamayla25-colourpop-main-squeeze-9-shade/',
                                  '/products/jar736-coming-soon-colourpop-87c5/',
                                  '/products/sa_ara-colourpop-miss-bliss-/',
                                  '/products/sa_ara-colourpop-its-my-pleasure/',
                                  '/products/sa_ara-colourpop-blue-moon-/',
                                  '/products/isabelle_rose-kylie-jenner-kylie-cosmetics-2/'])


class TestListingPageParse(unittest.TestCase):
    def setUp(self):
        with open("test/test_data/test_listing.html", "r", encoding="utf-8") as f:
            html = f.read()
        self.parser = DpopParser(html)

    def test_get_description(self):
        value = self.parser.get_listing_description()
        with open("test/test_data/description.html", "r", encoding="utf-8") as f:
            test_desc = f.read()
        self.assertEqual(value, test_desc)


class TestGetStats(unittest.TestCase):

    def setUp(self):
        values = [0, 2, 4, 6]
        self.results = DpopParser.get_stats(values)

    def test_get_stats_min(self):
        self.assertEqual(self.results["min"], 0)

    def test_get_stats_mean(self):
        self.assertEqual(self.results["mean"], 3)

    def test_get_stats_mode(self):
        self.assertEqual(self.results["mode"], 0)

    def test_get_stats_max(self):
        self.assertEqual(self.results["max"], 6)


class TestE2E(unittest.TestCase):
    def test_get_listing_info(self):
        with DpopScrape() as scrape:
            scrape.search("#colourpop the child")
            html = scrape.get_page_html()
            with open("out.html", "w") as f:
                f.write(html)
            links = DpopParser(html).get_links()
            listing_element = scrape.get_listing_element(links[0])
            listing_html = scrape.get_listing_info(listing_element)
            listing_desc = DpopParser(listing_html).get_listing_description()

        with open("test/test_data/test_listing.html", "r", encoding="utf-8") as f:
            test_desc = f.read()

        self.assertEqual(listing_desc, test_desc)


if __name__ == '__main__':
    unittest.main()
