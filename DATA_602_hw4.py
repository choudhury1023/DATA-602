import urllib2
from bs4 import BeautifulSoup
from watson_developer_cloud import AlchemyLanguageV1

#Function to input url and extract body of the webpage
def getText(url):
    raw_text = urllib2.urlopen(url)
    soup = BeautifulSoup(raw_text.read(), 'html.parser')
    #Extract only the body of the text
    text = soup.find("div", { "class" : "body" }).get_text()

    return (text)


#Function to extract keywords 
def getKeywords(text):
    alchemyapi = AlchemyLanguageV1(api_key='247f89cb2bffb9028ae89e1398cffb08c8f49dc3')
    result = alchemyapi.keywords(text = text)
    keywords = result['keywords']

    return keywords


#Function to print result in desired format    
def printKeywords(keywords):
    #Print header
    print 'Top 10 Kywords'.center(40, '#')
    print 'Keyword'.ljust(30) + 'Relevance'
    #Pick top ten keywords
    for i in keywords[0:10]:
            print i['text'].ljust(30) + i['relevance']


# Main
if __name__ == "__main__":
    url = 'http://newcoder.io/scrape/intro/'
    text = getText(url)
    print text
    keywords = getKeywords(text)
    printKeywords(keywords)

"""References:
http://stackoverflow.com/questions/5041008/how-to-find-elements-by-class
http://python-reference.readthedocs.io/en/latest/docs/str/ljust.html
http://python-reference.readthedocs.io/en/latest/docs/str/center.html
"""
