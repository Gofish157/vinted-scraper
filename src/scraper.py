from bs4 import BeautifulSoup 
from selenium import webdriver as wd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from .config import OPTIONS
from .normalize import time_normalization, price_normalization, condition_normalization


def pick_text(soup, selector):
    elem = soup.select_one(selector)
    return elem.get_text(strip=True) if elem else None 

def pars_link(url: str, browser: wd) -> dict:

    browser.get(url)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="item-sidebar-price-container"]')))

    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
        
    a = pick_text(soup, '[data-testid="favourite-button"] span.web_ui__Text__text')
    likes_count = int(a if a != None else 0)

    price_with_fee = soup.select_one('[data-testid="item-sidebar-price-container"] button[aria-label*="€"]').get("aria-label").split("\xa0")[0]

    upload_date = pick_text(soup, '[data-testid="item-attributes-upload_date"] [itemprop="upload_date"] span')

    item_condition = pick_text(soup, '[data-testid="item-attributes-status"] [itemprop="status"] span')

    item_name = pick_text(soup, '[data-testid="item-page-summary-plugin"] h1')

    item_size = pick_text(soup, '[data-testid="item-attributes-size"] [itemprop="size"] span')

    item_status = "sold" if pick_text(soup, '[data-testid="item-status--content"]') else "available"

    return {
        "id": (url.split('/')[-1]).split('-')[0],
        "status": item_status,
        "name": item_name,
        "size": item_size,
        "likes": likes_count,
        "price": price_normalization(price_with_fee),
        "upload_time": time_normalization(upload_date),
        "item_condition": condition_normalization(item_condition),
        "link": url
    }


