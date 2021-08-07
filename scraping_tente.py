from bs4 import BeautifulSoup #pourquoi pas import bs4?
import requests

def scrap_one_product(url):
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        name = soup.find("h1", id="productTitle")
        price = soup.find("span", class_="price")
        informations = {'nom': name.text, 'prix': price.text}
        print(informations)
        return informations
    else:
        print("requête impossible")
        return{}

url = 'https://www.intent24.fr/Tente-pliante/'
def scraping_page_categorie(url):
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        produits = soup.find_all("div", class_="card")
        listproduct = []
        for produit in produits:
            link = produit.find("a").get("href")
            information_produits = scrap_one_product(link)
            listproduct.append(information_produits)
        print(listproduct)
    else:
        print('requête impossible')

def scrap_all_category(url):
    response = requests.get(url)
    url = 'https://www.intent24.fr/Tente-pliante/'
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        li = soup.find("ul", _class="pagination").find_all("a")
        page_number = li[5]
        print(page_number)
        i=0
        while i = 0:
            page_url = url
            i=i+1
            continue
        while i < page_number and > 0:
            page_url = url + '?pgNr=' + str(i)
            print(scraping_page_categorie(page_url))
            i=i+1
scrap_all_category('https://www.intent24.fr/Tente-pliante/')