from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def dpop_search(driver, search_term):
    driver.get('https://www.depop.com/search')
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys(f'{search_term}')
    elem.send_keys(Keys.RETURN)

    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

    return html


if __name__ == "__main__":
    driver = webdriver.Chrome()
    page_html = dpop_search(driver, "main squeeze eyeshadow palette")
    driver.close()
