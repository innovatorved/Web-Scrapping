# tag 
"""
Tag Objects

A HTML tag is used to define various types of content. A tag object in BeautifulSoup corresponds to an HTML or XML tag in the actual page or document.

Tags contain lot of attributes and methods and two important features of a tag are its name and attributes.

"""
from bs4 import BeautifulSoup

soup = BeautifulSoup('<b class="boldest">Ved Prakash Gupta</b>' , "lxml")
# when we pass html.parser then we not change into tag
print(soup) 
# output : <body><b class="boldest">Ved Prakash Gupta</b></body>

print(soup.name)
# Output : '[document]'

tag = soup.html #change doc in to html tag 
print(tag.name)
# Output : 'html'

print(type(tag))
# Output : <class 'bs4.element.Tag'>

tag.name = "small" 
print(tag)
# Output : <small><body><b class="boldest">Ved Prakash Gupta</b></body></small>

print(tag.name) # Output : "small" 
