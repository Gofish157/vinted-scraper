import pandas as pd

from .scraper import pars_link
from .crawler import url_list



URL = "https://www.vinted.sk/catalog/2050-clothing"

items = []
i = 0
for url in url_list(URL):
    i+=1
    items.append(pars_link(url))
    if i == 5: break

df = pd.DataFrame(items)

print(df)

