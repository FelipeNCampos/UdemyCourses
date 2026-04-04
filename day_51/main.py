from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time 
twiter_url="https://x.com/home"
speedTeste_url="https://www.speedtest.net/pt"


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


