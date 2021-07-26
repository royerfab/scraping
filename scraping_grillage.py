from bs4 import BeautifulSoup #pourquoi pas import bs4?
import requests

def scrap_one_product(url):
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        name = soup.find("h1", class_="product_title entry-title")
        price = soup.find("span", class_="woocommerce-Price-amount amount")
        description = soup.find("div", class_="col-md-12")
        informations = {'nom': name.text, 'prix': price.text, 'description': description.text}
        print(informations)
        return informations
    else:
        print("requête impossible")
        return{}

url = 'https://clotures-grillages.com/catalogue/grillage-rigide/kit-grillages-rigides/?sort=publish_date:DESC'
def scraping_page_categorie(url):
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        produits = soup.find_all("div", class_="col-xs-6 col-md-3 product--item")
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
    base_url = 'https://clotures-grillages.com/catalogue/grillage-rigide/kit-grillages-rigides/?sort=publish_date:DESC&offset='
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        page_number = len(soup.find("div", class_='search--pagination').find_all("a"))
        print(page_number)
        i=0
        while i < page_number:
            page_url = base_url + str(i)
            print(scraping_page_categorie(page_url))
            i=i+1
scrap_all_category('https://clotures-grillages.com/catalogue/grillage-rigide/kit-grillages-rigides/?sort=publish_date:DESC')