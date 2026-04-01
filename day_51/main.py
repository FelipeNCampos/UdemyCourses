from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time 
twiter_url="https://x.com/home"
speedTeste_url="https://www.speedtest.net/pt"

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

def get_required_env(name):
    env_value = os.getenv(name) or ENV_VALUES.get(name)

    if env_value:
        return env_value

    raise KeyError(f"Missing required setting: {name}")

ENV_PATH = Path(__file__).with_name(".env")
ENV_VALUES = load_env_values(ENV_PATH)



config = webdriver.ChromeOptions()  

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
config.add_argument(f"--user-data-dir={user_data_dir}")

config.add_experimental_option("detach", True)

drive = webdriver.Chrome(options=config)
drive.implicitly_wait(3)


drive.get(speedTeste_url)

drive.find_element(By.CLASS_NAME, "start-text").click()

time.sleep(40)
download = float(drive.find_element(By.CLASS_NAME, "result-data-large").text)
upload = float(drive.find_element(By.CLASS_NAME, "upload-speed").text)


print(f"download = {download}, upload = {upload}")

if download < 600 or upload < 20:
     drive.get(twiter_url)
     drive.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block").send_keys(f"I pay for 600/20 and only receive {download}/{upload}!")


