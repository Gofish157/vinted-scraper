from bs4 import BeautifulSoup 
from urllib.parse import urljoin
from selenium import webdriver as wd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from .config import OPTIONS, BASE

ITEM_LINKS = (By.CSS_SELECTOR, 'a[href*="/items/"]')


def url_list(url: str) -> list[str]:
    items = list()
    browser = wd.Chrome(options=OPTIONS)
    try:
        browser.get(url)
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-testid*="product-item-id"]')))
        html = browser.page_source
        soup = BeautifulSoup(html, 'lxml')
        cards = soup.select('[data-testid*="product-item-id"]')
        for card in cards:
            a = card.select_one('a[href]')
            if a:
                href = urljoin(BASE, a.get('href'))
                if href:
                    items.append(href)
                    print(href)
        return items
    finally:
        browser.quit()
    