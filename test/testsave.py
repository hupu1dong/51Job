from bs4 import BeautifulSoup
import xlwt
import urllib.request,urllib.error
import re
import sqlite3
from urllib import parse
from lxml import etree

detail = etree.parse("detail.html",'gbk')
jobname = detail.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/h1')
print(jobname)
salary = detail.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/strong')
print(salary)
location = detail.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[1]/a[1]')
print(location)