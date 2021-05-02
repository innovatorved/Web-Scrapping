# python b6-comment.py

from bs4 import BeautifulSoup

with open("example.html" ,"r") as l:
	soup = BeautifulSoup(l ,"lxml")
	
comment = soup.p.string
print(comment)
print(type(comment))
print(soup.p.prettify())