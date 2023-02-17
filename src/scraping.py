import requests
from bs4 import BeautifulSoup

website = 'https://index.hu'

# Kereset kulcsszavak
keywordsList = ["Orbán", "forint", "Szijjártó"]
maxArticles = 10

def index(website, keywordsList, maxArticles):
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    cikkek = soup.find_all('h2', attrs={'class':'cikkcim'})
    otpChecker(cikkek, keywordsList, maxArticles)

def otpChecker(cikkek, keywordsList, maxArticles):
    count = 0
    for link in cikkek:
        if count <= maxArticles:
            for key in keywordsList:
                if key in link.find('a').get_text():
                    cikkCim = link.find('a').get_text()
                    cikkLink = link.find('a').get('href')
                    print(cikkCim)
                    print(cikkLink)
                    print("-------------------")
        else:
            print("--Meghivás más honlapon is.--")
            break
        count = count + 1

index(website, keywordsList, maxArticles)