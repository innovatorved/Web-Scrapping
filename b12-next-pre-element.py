# python b12-next-pre-element.py
"""
.next_elements and .previous_elements
We use these iterators to move forward and backward to an element.
"""
from bs4 import BeautifulSoup

html = """<a class="prog" href="https://www.tutorialspoint.com/ruby/index.htm" id="link5">C</a>
"""

soup = BeautifulSoup(html , "lxml")

print(soup.a.next_element)
print("\n\n",list(soup.a.next_element.previous_elements))