
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

options = Options()
options.headless = True


class DpopScrape:
    def __init__(self, driver=None, headless=False):
        if driver:
            self.driver = driver
        else:
            options = Options()
            options.headless = headless
            self.driver = webdriver.Chrome(chrome_options=options)
            self.driver.set_window_size(1080, 800)

        self.state = "unknown"

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        self.driver.close()

    def search(self, search_term):
        self.driver.get('https://www.depop.com/search')
        time.sleep(1)
        self.state = "SEARCH"
        elem = self.driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys(f'{search_term}')
        elem.send_keys(Keys.RETURN)
        time.sleep(1)

    def get_listing_element(self, name):
        if not self.state == "SEARCH":
            raise Exception(
                f"Invalid browser state. should be SEARCH but was { self.state }")
        return self.driver.find_element_by_xpath(f"//a[contains(@href,'{ name }')]")

    def get_listing_info(self, element):
        if not self.state == "SEARCH":
            raise Exception(
                f"Invalid browser state. should be SEARCH but was { self.state }")
        start_url = self.driver.current_url
        element.click()
        time.sleep(1)
        html = self.get_page_html()
        self.driver.back()
        time.sleep(1)
        if start_url != self.driver.current_url:
            raise Exception("Page nav failure")
        return html

    def get_page_html(self):
        return self.driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
