""" def index(website, keywordsList, maxArticles):
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    cikkek = soup.find_all('h2', attrs={'class':'cikkcim'})
    otpChecker(cikkek, keywordsList, maxArticles) """