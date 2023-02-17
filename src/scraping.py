import requests
from bs4 import BeautifulSoup

# Newspages
websites = ["https://index.hu", "https://portfolio.hu"]

# Keywords
keywordsList = ["Deviza", "Forint", "forint", "Tőzsd", "Otp", "Richter"]

# Maximum number of displayed articles
maxArticles = 10

def main(websites, keywordsList, maxArticles):
    for website in websites:
        result = requests.get(website)
        content = result.text
        soup = BeautifulSoup(content, 'lxml')
        tags = ["h1", "h2", "h3"]
        for h in tags:
            articles = soup.find_all(h)
            Checker(website, articles, keywordsList, maxArticles)
    

""" def index(website, keywordsList, maxArticles):
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    cikkek = soup.find_all('h2', attrs={'class':'cikkcim'})
    otpChecker(cikkek, keywordsList, maxArticles) """


def Checker(website, articles, keywordsList, maxArticles):
    count = 0
    for link in articles:
        if count <= maxArticles:
            for key in keywordsList:
                if key in link.find('a').get_text(): 
                # if any(key.startswith(key) for key in link.find('a').get_text()):
                    articleTitle = link.find('a').get_text()
                    articleLink = link.find('a').get('href')
                    print("-------------------")
                    print(articleTitle)
                    print(articleLink)
                    print(website)
                    print("-------------------")
        count = count + 1

# for test_word in search_words:
#	if any(word.startswith(test_word) for word in forbidden_list):
#    	print(test_word)


main(websites, keywordsList, maxArticles)