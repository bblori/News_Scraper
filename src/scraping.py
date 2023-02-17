import requests
from bs4 import BeautifulSoup

website = 'https://index.hu'

result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

# print(soup.prettify())
cikkek = soup.find_all('h2', attrs={'class':'cikkcim'})

# Kereset kulcsszavak
keywordsList = ["Otp"]
count = 0
maxArticles = 5


for link in cikkek:
    if count <= maxArticles:
        cikkCim = link.find('a').get_text()
        cikkLink = link.find('a').get('href')
        print("-------------------")
    else:
        break
    count = count + 1


