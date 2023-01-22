from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

link = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

browser = webdriver.Chrome("chromedriver.exe")
browser.get(link)

Headerlist = ["Name", "Light_Years_from_Earth", "Planet_Mass", "Stellar_Magnitude", "Discovery_Date"]
planetData = []

def Scrape1():
    for i in range(210):
        GoodSoup = BeautifulSoup(browser.page_source, "html.parser")
        for ultag in GoodSoup.find_all("ul", attrs={"class", "exoplanet"}):
            litag = ultag.find_all("li")
            templist = []
            for i, lit in enumerate(litag):
                if i==0:
                    templist.append(lit.find_all("a")[0].contents[0])
                else:
                    try:
                        templist.append(lit.contents[0])
                    except:
                        templist.append("")
            planetData.append(templist)
    with open("Planet.csv","w",newline="") as f:
        obj = csv.writer(f)
        obj.writerow(Headerlist)
        obj.writerows(planetData)
    

Scrape1()

