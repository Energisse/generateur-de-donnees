'''Fonction module contient les fonctions du générateur textuelle.'''

# includes
import requests
import pdfkit
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

# function
def get_html_from_url(url):
    '''Retourne une soup correspondante au paramètre url.'''
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    return soup

def extrac_elem(soup, tag, url):
    '''Retourne une liste qui contien tous les éléments HTML correspondant au paramètre tag dans paramètre soup.'''
    ls_elem = soup.find_all(tag)

    if tag == "img":
        for element in ls_elem:
            # convertir le lien en lien avec http
            element["srcset"] = ""
            link = element["src"]
            if link[0] == "/":
                if link[1] == "/":
                    element["src"] = "https:" + link
                else:
                    element["src"] = "https://" + url.split("/")[2] + link

    return ls_elem

def create_file(ls_elem, output_file_name, extention):
    '''Créer les trois fichiers nommés paramètre output_file_name qui contient tous les éléments dans paramètre ls_eleme.'''
    # créé la stucture html
    soup = BeautifulSoup()
    html = soup.new_tag('html')
    soup.append(html)
    head = soup.new_tag('head')
    soup.html.append(head)
    body = soup.new_tag('body')
    soup.html.append(body)
    # remplir le body avec les éléments récupéré
    for elem in ls_elem:
        if elem.name == "title":
            soup.html.body.append("{{ title: " + elem.getText() + " }}")

        elif extention == "txt" and elem.name == "img":
            soup.html.body.append("{{ alt: " + elem['alt'] + ", src: " + elem['src'] + " }}\n")

        elif extention == "txt" and elem.name == "table":
            soup.html.body.append("{{ table: " + MarkdownConverter().convert_soup(elem) + " }}\n")
            
        else:
            soup.html.body.append(elem)

    if extention == "txt":
        with open(output_file_name + "." + extention, "w") as file:
            file.write(soup.getText())

    if extention == "html":
        with open(output_file_name + "." + extention, "w") as file:
            file.write(soup.prettify())

    if extention == "pdf":
        pdfkit.from_string(soup.prettify(), output_file_name + "." + extention)

def trier_element(ls_elem):
    '''Trier paramètre ls_elem du premier au dernier croisé.'''
    ls_elem_sorted = []
    for i in range(len(ls_elem)):
        premier = ls_elem[0]
        for elem in ls_elem:
            # trouver le premier
            if elem.sourceline == premier.sourceline \
            and elem.sourcepos < premier.sourcepos \
            or elem.sourceline < premier.sourceline:
                premier = elem
        # ajouter premier à ls_elem_sorted
        ls_elem.remove(premier)
        ls_elem_sorted.append(premier)

    return ls_elem_sorted