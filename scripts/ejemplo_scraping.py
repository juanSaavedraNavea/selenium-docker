from utils.browser import get_driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time

load_dotenv()

URL = os.getenv("URL_DE_PRUEBA", "https://example.org")

def main():
    driver = get_driver()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get(URL)
        # Espera un elemento (ejemplo genérico: h1)
        h1 = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
        print("Título:", h1.text)

        # Tu lógica de scraping aquí...
        time.sleep(30)

    except TimeoutException:
        print("Timeout esperando elementos.")
    except NoSuchElementException:
        print("No se encontró el elemento solicitado.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
