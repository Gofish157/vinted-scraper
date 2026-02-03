from selenium.webdriver.chrome.options import Options

BASE = "https://www.vinted.sk"

OPTIONS = Options()
OPTIONS.add_argument('--headless=new')
OPTIONS.add_argument('--lang=en-US')
OPTIONS.add_experimental_option("prefs", {
    "intl.accept_languages": "en,en-US"
})

