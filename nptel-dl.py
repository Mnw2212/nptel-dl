import urllib2
from bs4 import BeautifulSoup

import re
class Branches:

	def StreamList():
		'''
			Returns a list of the all the available Branches or streams
			Along with that return a dictionary of all the courses
			dict = {'CourseName':'url'}
		'''
		htmltext=urllib2.urlopen("http://www.nptel.ac.in").read()
		x = soup.find_all('a',style="border:thin", solid="")
		x = x[4:]
		CourseList=dict()
		Courses=[]
		for link in x:
			CourseList.update({link.contents[0].encode('ascii'):link.get('href')})
			Courses.append(link.contents[0].encode('ascii'))

		return Courses,CourseList

	def CourseList(self):
		htmltext = urllib2.urlopen("http://nptel.ac.in/courses.php?disciplineId=106")
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
		print final_arr[8][4]
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

final = Branches()
course = final.CourseList()
Link = final.DownloadLink(course)
