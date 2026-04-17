from bs4 import BeautifulSoup
from pathlib import Path
import re
import requests
import dotenv
import os

dotenv.load_dotenv(Path(__file__).resolve().with_name(".env"), override=True)

def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the HTML: {e}")
        return None
    

    
    
def processHTML(html):
    soup = BeautifulSoup(html, 'html.parser')

    listas = soup.find_all("ul")
    itens = listas[2].find_all("li", recursive=False)
    content = []
    for c in itens:
        adress_tag = c.find("address")
        address = adress_tag.get_text(strip=True) if adress_tag else "Address not found"
      
        price_tag = c.find("span", class_="PropertyCardWrapper__StyledPriceLine")
        raw_price = price_tag.get_text(" ", strip=True) if price_tag else ""
        price_match = re.search(r"\$[\d,]+", raw_price)
        price = price_match.group(0) if price_match else "Price not found"
        price = price.replace(",", ".")
        a_tag = c.find("a")
        link = a_tag["href"] if a_tag else "Link not found"    
      

        content.append([address,price,link])    
    for c in content:
        print(c)
        
    return content
    
    
    
    
    
def getContent():

    url = os.getenv("TARGET_URL")

    if not url:
        print("TARGET_URL is not set in the environment variables.")
        return None
    
    html = get_html(url)
    
    if html is None:
        return None
    
    return processHTML(html)
    
    
