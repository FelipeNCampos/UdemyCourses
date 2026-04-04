from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from pathlib import Path
import time 

perfil_url = "https://www.instagram.com/unificadaufg/"

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

    
if __name__ == "__main__":
    user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
    driverConfig = webdriver.ChromeOptions()
    driverConfig.add_argument(f"--user-data-dir={user_data_dir}")
    driverConfig.add_experimental_option("detach", True)
    
    drive = webdriver.Chrome(options=driverConfig)

    drive.get(perfil_url)
    drive.implicitly_wait(5)                
    seg = drive.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/section/main/div/div/header/div/section[2]/div[1]/div[3]/div[2]/a/span")
    seg.click()
    total = int(seg.text.split()[0].replace(".", ""))        
    print(f"Total de seguidores: {total}")
    registro = []
    print("iniciando seguir os seguidores...")
    for c in range(total):
        try:
            nome = drive.find_element(By.XPATH, f"/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{c+1}]/div/div/div/div[2]/div/div/div/div/span/div/a/div/div/span").text
                                                        #    /html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div/div/div/div/span/div/a/div/div/span
                                                        #    /html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div/span/div/a/div/div/span
            print(f"Seguidor {c+1}: {nome}")
        except:
            print("Erro ao encontrar o nome do seguidor")
            continue
        try: 
            botao = drive.find_element(By.XPATH, f"/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{c+1}]/div/div/div/div[3]/div/button")
        except:
            print("Erro ao encontrar o botão de seguir")
            continue
        if botao.text == "Seguir":
            try:
                
                botao.click()
                print('\n----------\nSeguindo: ', nome)
                registro.append(nome)
            except:
                print("Erro ao clicar no botão de seguir")
        drive.execute_script("arguments[0].scrollTop += 100", drive.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"))

        time.sleep(0.3)

        
    drive.quit()
        