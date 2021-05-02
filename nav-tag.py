# python nav-tag.py

#NavigableString
"""
The navigablestring object is used to represent the contents of a tag. To access the contents, use “.string” with tag."""


html = """<div id ="class1">MY Name</div>"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html , "lxml")

# print(soup)
print(soup.string)
print(type(soup.string))

#  replace tring
soup.string.replace_with("Ved Prakash Gupta")
# soup.string = "hlkok"
print(soup)
print(soup.string)