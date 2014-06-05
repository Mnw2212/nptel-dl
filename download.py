from bs4 import BeautifulSoup
import urllib2

def Download():
	htmltext = urllib2.urlopen("file:///home/mayuresh/Desktop/nptel-dl/NPTEL    Computer Science and Engineering - Logic for CS.html")
	soup = BeautifulSoup(htmltext)
	x = soup.find_all('div',id='tab3')
	soupAgain = BeautifulSoup(str(x[0]))
	y = soupAgain.find_all('p')
	urls = soupAgain.find_all('a')
	for link in y:
		print link.contents[0]

	for url in urls:
		print url.get('href')


Download()