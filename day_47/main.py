import os
from pathlib import Path
import smtplib as emailer
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


ENV_PATH = Path(__file__).with_name(".env")


def load_env_values(path):
    env_values = {}

    if not path.exists():
        return env_values

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()

        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        env_values[key.strip()] = value.strip().strip('"').strip("'")

    return env_values


ENV_VALUES = load_env_values(ENV_PATH)


def get_required_env(name):
    env_value = os.getenv(name) or ENV_VALUES.get(name)

    if env_value:
        return env_value

    raise KeyError(f"Missing required setting: {name}")


# Configurações do Selenium (modo headless)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Caminho do chromedriver deve estar no PATH ou na mesma pasta do script
url = "https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=pd_rhf_dp_s_pd_sbs_rvi_d_sccl_2_1/147-7959429-9960429?pd_rd_w=R4zwd&content-id=amzn1.sym.6640a844-ab24-4352-ac9b-78899e683a5e&pf_rd_p=6640a844-ab24-4352-ac9b-78899e683a5e&pf_rd_r=9QBNJSFQSHQKNZSYMQ58&pd_rd_wg=EM0qY&pd_rd_r=a4de28fc-9f6d-45ce-aef0-901bf8e4f6ff&pd_rd_i=B00FLYWNYQ&th=1"

with webdriver.Chrome(options=chrome_options) as driver:
    driver.get(url)
    sleep(4)  # Aguarda o carregamento da página
    try:
        dol_elem = driver.find_element(By.CLASS_NAME, "a-price-whole")
        cents_elem = driver.find_element(By.CLASS_NAME, "a-price-fraction")
        dol_text = dol_elem.text.replace(",", "").replace(".", "")
        cents_text = cents_elem.text
        full_price = float(f"{dol_text}.{cents_text}")
        print(full_price)
        if full_price < 110:
            with emailer.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(
                    user="felipe.n.cmp@gmail.com",
                    password=get_required_env("SMTP_PASSWORD"),
                )
                connection.sendmail(
                    from_addr="felipe.n.cmp@gmail.com",
                    to_addrs="felipe_nunes@discente.ufg.br",
                    msg=f"Subject:Alerta de preço da amazon!\n\nO preço da panela agora é {full_price}".encode("utf-8"),
                )
        else:
            print("wait!")
    except Exception as e:
        print("Preço não encontrado na página com Selenium. O HTML pode ter mudado ou o scraping foi bloqueado.")
        print(e)
