import urllib.request
import os
import re
from bs4 import BeautifulSoup

def parse_full_archive(url):
	if os.path.isfile("aaronsw.html"):
		os.remove("aaronsw.html")
	file = open("aaronsw.html","a")
	posts = []
	soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')

	for link in soup.find_all("a"):
		if link["href"] != "./" and link["href"] != "/":
			posts.append(link["href"])
			link["href"] = "#" + link["href"]
		else:
			link["href"] = "#"

	file.write(soup.prettify(formatter="html"))

	print('parsed TOC')

	for post in posts:
		file.write(parse_single_post(post))

	file.close()

def parse_single_post(post):
	try:
		print('parsing post',post)
		soup = BeautifulSoup(urllib.request.urlopen("http://www.aaronsw.com/weblog/"+post).read(), 'html.parser')
		for e in soup.find_all("script"):
			e.decompose()
		for a in soup.find_all("div",{"id": "comments_body"}):
			a.decompose()
		soup.find("p", {"class": "footertag"}).decompose()
		soup.find("h1", {"class": "title"}).decompose()
		# soup.find("i", text=re.compile("You should follow me on twitter")).decompose()
		print('parsed post',post)
		return "<a name=\""+post+"\">" + soup.prettify(formatter="html")
	except Exception as e:
		print('failed post',post,e)
		return "<a name=\""+post+"\">Not found."

parse_full_archive('http://www.aaronsw.com/weblog/fullarchive')