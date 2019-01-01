import requests
from bs4 import BeautifulSoup
data = requests.get("https://timesofindia.indiatimes.com/rss.cms")
soup = BeautifulSoup(data.text, 'html.parser')
for link in soup.find_all('a'):
    if link.get('class') == ['rssurl'] :
        link2 = link.get('href')
        data2 = requests.get(link2)
        soup2 = BeautifulSoup(data2.text, "lxml-xml")
        if soup2.item != None:
            print(soup2.item.title.string)
