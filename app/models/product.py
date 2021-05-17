import requests
from bs4 import BeautifulSoup





class Product:
    def __init__(self, product_id, product_name = None, opinions = []):
        self.product_id = product_id
        self.product_name = product_name
        self.opinions = opinions

    def extract_product(self):
        next_page = "https://www.ceneo.pl/{}#tab=reviews".format(self.product_id)

        while next_page:
            respons = requests.get(next_page)
            page_dom = BeautifulSoup(respons.text, "html.parser")
            opinions = page_dom.select("div.js_product-review")
            for opinion in opinions:
                opinion_elements = {key:extract_element(opinion, *args)
                                    for key, args in selectors.items()}
                opinion_elements["opinion_id"] = opinion["data-entry-id"]
                opinion_elements["recommendation"] = True if opinion_elements[
                    "recommendation"] == "Polecam" else False if opinion_elements["recommendation"] == "Nie polecam" else None
                opinion_elements["stars"] = float(opinion_elements["stars"].split("/")[0].replace(",", "."))
                opinion_elements["purchased"] = bool(opinion_elements["purchased"])
                opinion_elements["useful"] = int(opinion_elements["useful"])
                opinion_elements["useless"] = int(opinion_elements["useless"])
                self.opinions.append(opinion_elements)
            try:
                next_page = "https://www.ceneo.pl" + \
                page_dom.select("a.pagination__next").pop()["href"]
            except IndexError:
                next_page = None
            print(next_page)


     def __str__(self):
        pass

    def __dict__(self):
        pass


