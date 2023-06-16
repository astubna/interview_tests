# my solution of interview test: try to webscrape listings on the following webpage https://ovocnesady.sk/ponuka-bytov

import requests

from selenium import webdriver
import chromedriver_binary
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
domy=[] 
typy=[] 
cisla=[]
poschodia=[]
dispozicie=[]
stvorceInterier=[]
stvorceExterier=[]
kobky=[]
ceny=[]
splatky=[]
dostupnosti=[]


driver.get("https://ovocnesady.sk/ponuka-bytov")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll("td", attrs={"class": "views-field views-field-field-building-name"}):
    dom=a.find("a")
    domy.append(dom.text)

for a in soup.findAll("td", attrs={"class": "views-field views-field-field-unit-type"}):
    typ=a.find("a")
    typy.append(typ.text)

for a in soup.findAll("td", attrs={"class": "views-field views-field-field-flat-internal-id"}):
    cislo=a.find("a")
    cisla.append(cislo.text)

for a in soup.findAll("td", attrs={"class": "views-field views-field-field-floor-number"}):
    poschodie=a.find("a")
    poschodia.append(poschodie.text)

for a in soup.findAll("td", attrs={"class": "views-field views-field-field-flat-disposition"}):
    dispozicia=a.find("a")
    dispozicie.append(dispozicia.text)

for a in soup.findAll("td", attrs={"class": "views-field views-field-field-flat-area"}):
    interier=a.find("a")
    stvorceInterier.append(interier.text)

for a in soup.findAll("td", attrs={"class": "views-field views-field-field-flat-area-exterior"}):
    exterier=a.find("a")
    stvorceExterier.append(exterier.text)

for a in soup.findAll("td", attrs={"class": "views-field views-field-field-flat-area-cellar"}):
    kobka=a.find("a")
    kobky.append(kobka.text)

for a in soup.findAll("td", attrs={"class": "views-field views-field-field-flat-price-assoc"}):
    cena=a.find("a")
    ceny.append(cena.text)

for a in soup.findAll("td", attrs={"class": "views-field views-field-field-monthly-mortgage-payment"}):
    splatka=a.find("a")
    splatky.append(splatka.text)

for a in soup.findAll("td", attrs={"class": "views-field views-field-field-flat-availability"}):
    dostupnost=a.find("a")
    dostupnosti.append(dostupnost.text)

df = pd.DataFrame({'Bytový dom':domy, 'Typ':typy, 'Číslo bytu':cisla, 'Počet izieb':dispozicie, "Interiér":stvorceInterier, "Exteriér":stvorceExterier, "Kobka": kobky, "Cena s DPH":ceny, "Mesačná splátka":splatky, "Dostupnosť":dostupnosti}) 
df.to_csv('ovocnesady.csv', index=False, encoding='utf-8')