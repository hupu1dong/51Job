import re
import xlwt
from bs4 import BeautifulSoup

html = open("tmp.html","r")
bs = BeautifulSoup(html,"html.parser")
scr = str(bs.find_all('script'))
# print(scr)
findLink = re.compile(r'"job_href":"(.*?)",')
links = re.findall(findLink,scr)
for link in links:
    print(link)
