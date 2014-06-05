import urllib2
from bs4 import BeautifulSoup

import re

def StreamList():
'''
	Returns a list of the all the available Branches or streams
	Along with that return a dictionary of all the courses 	
	dict = {'CourseName':'url'}
'''

  htmltext=urllib2.urlopen("file:///home/mayuresh/Desktop/nptel-dl/IITs and IISc elearning Courses in Engineering and Science under NPTEL.html").read()
  soup=BeautifulSoup(htmltext)
  x = soup.find_all('a',style="border:thin", solid="")
  x = x[4:]
  CourseList=dict()
  Courses=[]
  for link in x:
     CourseList.update({link.contents[0].encode('ascii'):link.get('href')})
     Courses.append(link.contents[0].encode('ascii'))

  return Courses,CourseList



def CourseList():
'''
	Return a list of all the courses and their details
	List format is 
	final = [['Subject',
		 'ContentType',
		 'Prof. Name',
		 'University',
		 'ContentUrl',
		 ],[...]]
	
'''
  htmltext = urllib2.urlopen("file:///home/mayuresh/Desktop/nptel-dl/phase2.html")
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
  return final_arr
