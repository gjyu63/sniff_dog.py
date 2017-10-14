import urllib2
import re
from bs4 import BeautifulSoup


# response = urllib2.urlopen("http://catalog.registrar.ucla.edu/ucla-catalog2017-348.html")

# dirResponse = urllib2.urlopen("http://catalog.registrar.ucla.edu/ucla-catalog2017-159.html")

# test = urllib2.urlopen("http://catalog.registrar.ucla.edu/ucla-catalog2017-222.html")
# # m = re.findall ( '<span class="coursetitle">(.*?)</span>', response.read(), re.DOTALL)

# # for x in m:
# #     print x, '\n'

# # csurl = re.findall('<a class="main" href="(.*?)">Computer Science</a></td>', response.read(), re.DOTALL)

# # csurl = re.findall(r"href=\"(ucla-catalog.*)<\/a>", dirResponse.read(), re.DOTALL)

# csurl = test.read().find("Lower-Division Courses")

# print csurl


#m = re.findall ( '<span class="coursetitle">(.*?)</span>', response.read(), re.DOTALL)
urlist = []
for i in range(164, 926):
    pendingurl = "http://catalog.registrar.ucla.edu/ucla-catalog2017-" + str(i) + ".html"
    pendingpage = urllib2.urlopen(pendingurl).read()

    if pendingpage.find("hour") >= 0 and (pendingpage.find("Lower-Division Courses") >= 0 or pendingpage.find("Graduate Courses") >= 0) and pendingpage.lower().find("lecture") >= 0:
        urlist.append(pendingurl)

ofile=open("result.txt", "w")

for url in urlist:
    ofile.write("----------------------------------------------\n")
    response = urllib2.urlopen(url)
    m = re.findall ( '<span class="coursetitle">(.*?)</span>', response.read(), re.DOTALL)
    for ln in m:
        ofile.write(ln)
        ofile.write("\n\n")
