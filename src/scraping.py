import requests
from bs4 import BeautifulSoup


# Newspages
websites = ["https://index.hu", "https://portfolio.hu"]

# Keywords
keywordsList = ["Forint", "forint", "Tőzsd", "Otp", "Richter"]

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
    print("Vége a " + website + "-nak.")


def Checker(website, articles, keywordsList, maxArticles):
    count = 0
    for link in articles:
        if count <= maxArticles:
            # Searched keyword like: Otp in article title
            for key in keywordsList:
                if key in link.find('a').get_text():
                    articleTitle = link.find('a').get_text()
                    articleLink = link.find('a').get('href')
                    print("-----------\n" + articleTitle + "\n" + articleLink)
                    print("---------\n" + website)
        count = count + 1
    origoGetLinks(keywordsList, maxArticles)


def origoGetLinks(keywordsList, maxArticles):
    website = "https://origo.hu"
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    articles = soup.find_all('div', attrs={'ait-top'})
    for article in articles:
        articleTitle = article.get_text()
        articleLink = article.find('a').get('href')
        compare(articleTitle, articleLink, keywordsList)


def compare(articleTitle, articleLink, keywordsList):
    for key in keywordsList:
        if key in articleTitle:
            print(articleTitle + " " + articleLink)


if __name__ == "__main__":
    main(websites, keywordsList, maxArticles)

# origoGetLinks(keywordsList, maxArticles)
