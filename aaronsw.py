import urllib.request
from bs4 import BeautifulSoup
f = urllib.request.urlopen('http://www.aaronsw.com/weblog/tdk')
html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')

for e in soup.find_all("script"):
	e.decompose()

for a in soup.find_all("div",{"id": "comments_body"}):
	a.decompose()

soup.find("p", {"class": "footertag"}).decompose()

print(soup.prettify(formatter="html"))