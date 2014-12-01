class Downloader:
	def get_links(url):
		'''
		returns all the download links
		'''
		htmltext = urllib2.urlopen("url")
		soup = BeautifulSoup(htmltext)
		x = soup.find_all('div',id='tab3')
		soupAgain = BeautifulSoup(str(x[0]))
		y = soupAgain.find_all('p')
		urls = soupAgain.find_all('a')
		for link in y:
			print link.contents[0]

		for url in urls:
			print url.get('href')
		return url.get('href')

	def download(links,format="mp4"):
		'''
		Choose download links based on format requested.
		Default format is mp4
		Iteriate through all the links download.
		'''
