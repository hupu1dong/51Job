from bs4 import BeautifulSoup
'''
html = open("tmp.html","r")
bs = BeautifulSoup(html,"html.parser")

# resultList = bs.select("#j_joblist")
ediv = bs.select(".e > .el > .t")
print(ediv)
'''

html = open("detail.html","rb")
bs = BeautifulSoup(html,"html.parser")
# days = bs.select("div.cn > h1")[0]['title']
# print(days)
# salary = bs.select('div.cn > strong')[0].text
# print(salary)
# location = bs.select('div.cn > p.cname > a.catn')[0]['title']
# print(location)
days = bs.select("div.cn > p.msg.ltype")
day = days[0]["title"].strip()
print(day)
# print(days[0]["title"].split("|").strip())
info = days[0]["title"].split("|")
for inf in info:
    print(inf.strip())

print(info[1].strip()[0:-2])
ndata = bs.select(".cn > h1")
print(type(ndata))
for d in ndata:
    print(d["title"])
    print(type(d))