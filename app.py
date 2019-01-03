import requests
import time
from bs4 import BeautifulSoup
data = requests.get("https://timesofindia.indiatimes.com/rss.cms")
soup = BeautifulSoup(data.text, 'html.parser')
list1 =[]
len1=0
for link in soup.find_all('a'):
    if link.get('class') == ['rssurl'] :
        link2 = link.get('href')
        data2 = requests.get(link2)
        soup2 = BeautifulSoup(data2.text, "lxml-xml")
        if soup2.item != None:
            list1.append(soup2.item.title.string)
            len1=len1+1
for i in range(len1):
	print(list1[i])
	print("\n")
time.sleep(300)
while True:
	list2=[]
	for link in soup.find_all('a'):
		if link.get('class') == ['rssurl']:
			link3 = link.get('href')
			data3 = requests.get(link3)
			soup3 = BeautifulSoup(data3.text, "lxml-xml")
			if soup3.item != None:
				list2.append(soup3.item.title.string)
	for i in range(len1):
		if(list1[i] != list2[i]):
			print(list2[i])
			print("\n")
			list1[i]=list2[i]
	time.sleep(180)

