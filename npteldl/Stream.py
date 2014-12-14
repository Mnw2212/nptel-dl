import urllib2
import re
from bs4 import BeautifulSoup

class Stream:
    def StreamTup(self):
        '''
        Returns a list all the available streams of study on the nptel website.
        '''
        htmltext=urllib2.urlopen("http://nptel.ac.in/").read()
        soup=BeautifulSoup(htmltext)
        x = soup.find_all('a',style="border:thin", solid="")
        x = x[4:]
        strtup=[]
        for link in x:
            name = link.contents[0].encode('ascii')
            url = "http://nptel.ac.in/"+link.get('href')
            strtup.append((name,url))
        return strtup

    def StreamDict(self):
        '''
        Returns a list of the all the available Branches or streams
        Returna a dictionary of all the courses
        dict = {'CourseName':'url'}
        '''
        x=self.StreamTup()
        Courses=dict()
        for tup in x:
            Courses.update({tup[0]:tup[1]})
        return Courses

    def StreamTuple(self):
        '''
        Returns a list of the all the available Branches or streams
        '''
        x=selfStreamTup()
        Courses=[]
        for link in x:
            Courses.append(link.contents[0].encode('ascii'))

        return Courses

class Course:
    def courseByDiscipline(disciplineId):
        url = 'http://nptel.ac.in/showCourses.php'
        values = {' disciplineId':str(disciplineId)}
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        the_page = response.read()
        soup = BeautifulSoup(the_page)
        courseval = soup.find_all('tr')
        for i in range(1,len(courseval)):
            courselist = courseval[i].find_all('td')
            for j in range(len(courselist)):
                print courselist[j]

    def courseByInstitute(instituteId):
        url = 'http://nptel.ac.in/showCourses.php'
        values = {'instituteCode':str(instituteId)}
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        the_page = response.read()
        soup = BeautifulSoup(the_page)
        courseval = soup.find_all('tr')
        for i in range(1,len(courseval)):
            courselist = courseval[i].find_all('td')
            for j in range(len(courselist)):
                print courselist[j]
