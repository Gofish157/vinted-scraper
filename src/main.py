import pandas as pd

from .scraper import pars_link


inf = {}


URL = "https://www.vinted.sk/items/8081898077-tricko?referrer=catalog"

inf = pars_link(URL)

df = pd.DataFrame([inf])

print(df)

