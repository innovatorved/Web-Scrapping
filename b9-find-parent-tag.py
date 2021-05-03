# python b9-find-parent-tag.py
"""
.parent

To access the element’s parent element, use .parent attribute.
"""
html = "<title>Title of the Page</title>"

from bs4 import BeautifulSoup

soup = BeautifulSoup(html , "lxml")

print(soup.name)

title = soup.title
print(title)
print(title.parent)
print(title.parent.parent)