import os
from pathlib import Path

import dotenv
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

dotenv.load_dotenv(Path(__file__).resolve().with_name(".env"), override=True)


def fillForms(content):
    form_url = os.getenv("FORM_URL")

    if not form_url:
        raise ValueError("FORM_URL is not set in the environment variables.")

    if not content:
        raise ValueError("No content received to fill the forms.")

    options = webdriver.ChromeOptions()
    drive = webdriver.Chrome(options=options)
    wait = WebDriverWait(drive, 20)
    drive.get(form_url)

    for c in content:
        wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, 'input[type="text"]')) >= 3)
        inputs = drive.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
        address_input, price_input, link_input = inputs[:3]

        for field in (address_input, price_input, link_input):
            drive.execute_script('arguments[0].scrollIntoView({block: "center"});', field)
            ActionChains(drive).move_to_element(field).click(field).perform()

        address_input.send_keys(c[0])
        price_input.send_keys(c[1])
        link_input.send_keys(c[2])

        submit_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    'div[role="button"][aria-label="Submit"], div[role="button"][aria-label="Enviar"]',
                )
            )
        )
        submit_button.click()

        another_response = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//a[contains(., "Enviar outra resposta") or contains(., "Submit another response")]',
                )
            )
        )
        another_response.click()
