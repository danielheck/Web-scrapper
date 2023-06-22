import requests
from bs4 import BeautifulSoup

url = "https://scryfall.com/card/eld/329/korvold-fae-cursed-king"
page = requests.get(url)

#print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

result = soup.find(id="main")

#print(result.prettify)

card_legals = result.find_all("div", class_="card-legality-item")

for card_legal in card_legals:
    format_name = card_legal.find("dt")
    is_legal = card_legal.find("dd", class_="legal")
    print(format_name.text.strip())
    if is_legal == None:
        print("Not legal")
    else:
        print(is_legal.text.strip())
    print()
