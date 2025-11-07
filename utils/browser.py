import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

load_dotenv()

def get_chrome_options() -> Options:
    headless = os.getenv("HEADLESS", "true").lower() == "true"
    opts = Options()
    if headless:
        opts.add_argument("--headless=new")
    # Flags recomendadas en contenedores
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument("--disable-features=VizDisplayCompositor")
    opts.add_argument("--disable-features=NetworkService,NetworkServiceInProcess")

    # Si quieres un user-agent fijo:
    # opts.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    #                   "(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

    # Rutas explícitas (útil en Debian slim)
    chrome_bin = os.getenv("CHROME_BIN", "/usr/bin/chromium")
    opts.binary_location = chrome_bin

    return opts

def get_driver():
    """
    Devuelve un WebDriver listo:
    - Si SELENIUM_REMOTE_URL está definido -> Remote WebDriver
    - Si no, usa Chrome local + chromedriver
    """
    remote_url = os.getenv("SELENIUM_REMOTE_URL")
    options = get_chrome_options()

    if remote_url:
        # Remote (Selenium Grid o standalone:chromium)
        return webdriver.Remote(command_executor=remote_url, options=options)
    else:
        # Local (Chromium + chromedriver instalados en la imagen)
        driver = webdriver.Chrome(options=options)
        return driver
