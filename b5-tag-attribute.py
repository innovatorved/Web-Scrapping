# python b5-tag-attribute.py
from bs4 import BeautifulSoup

html = """
	<div class = "first">
	Hello Gentleman
	</div>
	<p class = "Second">
	My Name is Ved Gupta
	</p>
"""
# print(html)

soup = BeautifulSoup(html , "lxml")
# print(soup)
print(soup.name)

tag = soup.div
print(f"\nbefore changes :\n{tag}")  
# print(type(tag))
# change html of tag
# change class name and create style
tag['class'] = "fifth"
tag['style'] = "border:2px solid;"
print(f"\nAfter Changes :\n{tag}\n\n")

del tag['class']
del tag['style']
# del tag
print(f"After deleting  tags :\n{tag}")
