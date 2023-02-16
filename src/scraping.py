import requests
from bs4 import BeautifulSoup

website = 'https://index.hu'

result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

# print(soup.prettify())
cikkek = soup.find_all('h2', attrs={'class':'cikkcim'})

print(cikkek)
print(type(cikkek))

for link in cikkek:
#print(link.get_text())
#print(link.get('href')) """
    print(link.find('a').get_text())
    print("-------------------")

# for link in soup.find_all('a'):
#     print(link.get('href'))

# for i in box:
#     print(i.find('a').get_text())
#print(box)

