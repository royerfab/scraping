from bs4 import BeautifulSoup
import requests
from scraping_description import scrap_one_product
url = 'http://test-sites.octoparse.com/?product_cat=e-commerce-category-1'
def scraping_page_categorie(url):
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        produits = soup.find_all("li", class_="product")
        #que cherche-t-on exactement? Pourquoi ne pas mettre directement ce que l'on cherche? Pour contenir d'autres informations à l'intérieur
        print(len(produits))
        #doit-on forcément print(len(produits)) Non
        listproduct = []
        for produit in produits:
            #qu'est ce que produit et comment sait-on ce qu'est produit?
            # pourquoi recommencer à demander le nom et utiliser une fonction qui sert à trouver le nom? quelle différence avec la version d'avant?
            #doit-on écrire que lien=...? Pourtant h1 et h2 pas les mêmes titres.
            selector = "woocommerce-Price-amount amount"
            price = produit.find("span", class_="woocommerce-Price-amount amount")
            name = produit.find("h2", class_="woocommerce-loop-product__title")
            lien = produit.find("a").get("href")
            informationproduit = scrap_one_product(lien)
            listproduct.append(informationproduit)
        print(listproduct)


def scrap_all_category(url):
    response = requests.get(url)
    base_url = 'http://test-sites.octoparse.com/?product_cat=e-commerce-category-1&paged='
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        page_number = len(soup.find_all("a", class_="page-numbers"))-2
        i=0
        while i <= page_number:
            page_url = base_url + str(i) #du coup ici c'est page 0?
            print(scraping_page_categorie(page_url))
            i=i+1

scrap_all_category('http://test-sites.octoparse.com/?product_cat=e-commerce-category-1')
#où on met cette ligne?
#Fait-on une liste aussi?