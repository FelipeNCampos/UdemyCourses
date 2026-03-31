from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import os
from pathlib import Path
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

def get_required_env(name):
    env_value = os.getenv(name) or ENV_VALUES.get(name)

    if env_value:
        return env_value

    raise KeyError(f"Missing required setting: {name}")

ENV_VALUES = load_env_values(ENV_PATH)

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")


gym_url ="https://appbrewery.github.io/gym/"

drive = webdriver.Chrome(options=chrome_options)

drive.implicitly_wait(10)
drive.get(gym_url)






def choose_class(drive):
    try:
        dias: list[WebElement] = drive.find_elements(By.CLASS_NAME, "Schedule_dayGroup__y79__")
        for dia in dias:
            titulo = dia.find_element(By.CLASS_NAME,"Schedule_dayTitle__YBybs").text
            if "Tue" in titulo:
                cursosCards = dia.find_elements(By.CLASS_NAME, "ClassCard_cardHeader__D9pf3")
                for cursoCard in cursosCards:
                    titulo = cursoCard.find_element(By.CLASS_NAME, "ClassCard_className__q0kVz ")
                    horario = cursoCard.find_element(By.CLASS_NAME, "ClassCard_classDetail__Z8Z8f")
                    if "6:00 PM" in horario.text:
                        return {"bookButton":cursoCard.find_element(By.CLASS_NAME, "ClassCard_bookButton__DMM1I "), "title":titulo, "horario":horario}
                
    except NoSuchElementException:
        return {"status": 404, "result": None}

    
    
try:
    
    drive.find_element(By.CLASS_NAME, "Home_heroButton__3eeI3").click()

    email_input = drive.find_element(By.ID, "email-input")
    email_input.send_keys("felipe.n.cmp@gmail.com")
    password_input = drive.find_element(By.ID, "password-input")
    password_input.send_keys(get_required_env("PASSWORD"))

    drive.find_element(By.ID,"submit-button").click()
    resul = choose_class(drive)
    try:
        if resul['bookButton'].text == "Booked":
            print("Aula já agendada")
        elif resul['bookButton'].text == "Join Waitlist":
            resul['bookButton'].click()
            print("Aula adicionada à lista de espera")
        elif resul['bookButton'].text == "Book Class":
            resul["bookButton"].click()
            print(f"Aula: {resul['title'].text} agendada as {resul['horario'].text} ")
        else:
            print("Aula não encontrada")
    except:
        print("Erro ao tentar agendar a aula")
        
        
except:
    print("erro")