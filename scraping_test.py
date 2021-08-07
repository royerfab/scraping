from bs4 import BeautifulSoup
import requests

url = 'https://www.webscraper.io/test-sites/e-commerce/allinone/computers'
response = requests.get(url)
if response.ok:
    soup = BeautifulSoup(response.content, 'html.parser')
    description = soup.find("p", class_="description")
    #print(description.text)
    bouton = soup.find_all("button", class_="btn swatch")
    #print(bouton[2]
    produits = soup.find_all("div", class_="thumbnail")
    print(len(produits))
    links = []
    for produit in produits:
        selector = "pull-right price"
        price = produit.find-all("h4", class_=selector)
        allprice = produit.find_all("h4")
        link = allprice[1]
        links.append(link.find("a").get("href"))
        print("==========")

print(links)