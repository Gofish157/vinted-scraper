from selenium.webdriver.chrome.options import Options

OPTIONS = Options()
OPTIONS.add_argument('--headless=new')
OPTIONS.add_argument('--lang=en-US')
OPTIONS.add_experimental_option("prefs", {
    "intl.accept_languages": "en,en-US"
})