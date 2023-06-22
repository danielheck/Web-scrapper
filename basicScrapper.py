import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)


soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

#print(results.prettify)

jobElements = results.find_all("div", class_="card-content")

#for jobElement in jobElements:
 #   titleElement = jobElement.find("h2", class_="title")
  #  companyElement = jobElement.find("h3", class_="company")
   # locationElement = jobElement.find("p", class_="location")
    #print(titleElement.text.strip())
    #print(companyElement.text.strip())
    #print(locationElement.text.strip())
    #print()

pythonJobs = results.find_all("h2", string=lambda text: "python" in text.lower())

pythonJobElements = [ h2Element.parent.parent.parent for h2Element in pythonJobs]

for jobElement in pythonJobElements:
    titleElement = jobElement.find("h2", class_="title")
    companyElement = jobElement.find("h3", class_="company")
    locationElement = jobElement.find("p", class_="location")
    print(titleElement.text.strip())
    print(companyElement.text.strip())
    print(locationElement.text.strip())
    print()