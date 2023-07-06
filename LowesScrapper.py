import requests
from bs4 import BeautifulSoup

url = "https://www.lowes.com/pd/7-16-CAT-PS2-10-OSB-Sheathing-Application-as-4-x-8/50382768"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="main")


prices = results.find("div", class_="newPriceWrapper")

print(prices.prettify)

