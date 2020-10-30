
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver


def dpop_search(driver, search_term):
    driver.get('https://www.depop.com/search')
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys(f'{search_term}')
    elem.send_keys(Keys.RETURN)


def get_listing_info(driver: WebDriver, element):
    start_url = driver.current_url
    element.click()
    html = get_page_html(driver)
    driver.back()
    if start_url != driver.current_url:
        raise Exception("Page nav failure")
    return html


def get_page_html(driver):
    return driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")


if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    dpop_search(driver, "main squeeze eyeshadow palette")
    page_html = get_page_html(driver)
    driver.close()
