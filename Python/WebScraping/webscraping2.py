from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import csv

link = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

browser = webdriver.Chrome("chromedriver.exe")
browser.get(link)

Headerlist = ["Name", "Light_Years_from_Earth", "Planet_Mass", "Stellar_Magnitude", "Discovery_Date", "HyperLink", "Planet_Type", "Planet_Radius", "Orbital_Radius", "Orbital_Period", "Eccentricity"]
planetData = []

def Scrape1():
    for i in range(1, 6):
        while True:
            GoodSoup = BeautifulSoup(browser.page_source, "html.parser")
            pageno = int(GoodSoup.find_all("input", attrs={"class", "page_num"})[0].get("value"))
            if pageno<i:
                browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
            elif pageno>i:
                browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a').click()
            else:
                break
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
            hltag = litag[0]
            templist.append("https://exoplanets.nasa.gov/"+hltag.find_all("a", href=True)[0]["href"])
            planetData.append(templist)
        print("page", i, "scrape complete")


    
Scrape1()

#Scrape1 gets data from the source page
#Scrape2 gets data from the hyperlink page

newPlanetData = []
def Scrape2(hl):
    try:
        page = requests.get(hl)
        GoodSoup = BeautifulSoup(page.content, "html.parser")
        templist = []
        for tr in GoodSoup.find_all("tr", attrs={"class", "fact_row"}):
            td = tr.find_all("td")
            for tdtag in td:
                try:
                    templist.append(tdtag.find_all("div", attrs={"class", "value"})[0].contents[0])
                except:
                    templist.append("")
        newPlanetData.append(templist)
    except:
        Scrape2(hl)

for i, data in enumerate(planetData):
    Scrape2(data[5])
    print("Scraping at hyperlink", i)

final = []
for i, data in enumerate(planetData):
    newPlanet = newPlanetData[i]
    newPlanet = [i.replace("\n", "") for i in newPlanet]
    final.append(data + newPlanet)

with open("Final.csv","w",newline="") as f:
    obj = csv.writer(f)
    obj.writerow(Headerlist)
    obj.writerows(final)
