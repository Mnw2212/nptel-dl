class Stream:
	def StreamUrl():
		'''

		Returns a list all the available streams of study on the nptel website.

		'''
		htmltext=urllib2.urlopen("file:///home/mayuresh/Desktop/nptel-dl/IITs and IISc elearning Courses in Engineering and Science under NPTEL.html").read()
		soup=BeautifulSoup(htmltext)
		x = soup.find_all('a',style="border:thin", solid="")
		x = x[4:]
		return x


	def StreamDict():
		'''
			Returns a list of the all the available Branches or streams
			Returna a dictionary of all the courses
			dict = {'CourseName':'url'}
		'''
		x=StreamUrl()
		Courses=dict()
		for link in x:
			Courses.update({link.contents[0].encode('ascii'):link.get('href')})

		return Courses

	def StreamList():
		'''
			Returns a list of the all the available Branches or streams
		'''
		x=StreamUrl()
		Courses=[]
		for link in x:
			Courses.append(link.contents[0].encode('ascii'))

		return Courses

class Course:
	def CourseList(self,url):
		'''
		Lists of each course with the details of course.
		[[Course,
			ContentType,
			Prof,
			University,
			DownloadLink,
			...],
			[...]
		]
		'''
		htmltext = urllib2.urlopen(url)
		soup = BeautifulSoup(htmltext)
		table = soup.find_all('tr', valign="top")
		content_table = BeautifulSoup(str(table[0]))
		content_table = content_table.find_all('tbody')
		AvailableCourses = len(content_table[6])
		soup=BeautifulSoup(str(content_table[6]))
		soup.prettify()
		ind_content = soup.find_all('tr')

		final_arr=[]
		for i in range(len(ind_content)):
			tr=[]
			for j in range(6):
				try:
					tr.append(ind_content[i].contents[j].contents[0].encode('ascii'))
				except:
					continue
			final_arr.append(tr)
		print final_arr[8][ 4]
		return final_arr


	def DownloadLink(self,final_arr):
		for i in range(len(final_arr)):
			try:
				x = Soupify(final_arr[i][4])
				aTag = x.find_all('a')
				links = aTag[0].get('href')
			except:
				continue
			print links


def Soupify(string):
	return BeautifulSoup(string)
