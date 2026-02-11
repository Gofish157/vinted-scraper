import pandas as pd
import selenium.webdriver as wd

from .scraper import pars_link
from .crawler import url_list
from .config import OPTIONS

browser = wd.Chrome(options=OPTIONS)


URL = "https://www.vinted.sk/catalog?search_text=converse%20mu%C5%BEi"


urls = url_list(URL)
print("length:", len(urls))

items = []
fails = []

for i, url in enumerate(urls, 1):
    try:
        items.append(pars_link(url, browser))
        print(f'[{i}/{len(urls)}] - OK')
    except Exception as e:
        print(f"[{i}/{len(urls)}] fail: {url} -> {repr(e)}")
        fails.append((url, repr(e)))

print("parsed:", len(items), "failed:", len(fails))

browser.quit()
df = pd.DataFrame(data=items)
df.to_csv("vinted_items.csv", index=False, encoding="utf-8")

print(df)

