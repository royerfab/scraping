from bs4 import BeautifulSoup
import requests

def scrap_one_product(url):
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        description = soup.find("div",
                                class_="woocommerce-Tabs-panel woocommerce-Tabs-panel--description panel entry-content wc-tab")
        name = soup.find("h1", class_="product_title entry-title")
        price = soup.find("span", class_="woocommerce-Price-amount amount")
        # print(description.text, name.text, price.text.replace("$", ""))
        informations = {'description': description.text, 'nom': name.text, 'prix': price.text}
        print(informations)
        return informations
    else:
        print('requête non aboutie')
        return {}
#pourquoi pas d'url?
#pourquoi return?