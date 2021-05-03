# python b11-find-all-siblings.py
from bs4 import  BeautifulSoup
sibling_soup = BeautifulSoup("<a><b>TutorialsPoint</b><c><strong>The Biggest Online Tutorials Library, It's all Free</strong></b></a>" , "lxml")

print(sibling_soup.prettify())

"""
In the above doc, <b> and <c> tag is at the same level and they are both children of the same tag. Both <b> and <c> tag are siblings.

.next_sibling and .previous_sibling

Use .next_sibling and .previous_sibling to navigate between page elements that are on the same level of the parse tree:
"""

# lets find next sibling of b tag
print(f"\n\nnext sibling of b tag : {sibling_soup.b.next_sibling}")

print(f"\n\nprevious sibling of c tag : {sibling_soup.c.previous_sibling}")

# Note : two strings are not sibling_soup
b_str = sibling_soup.b.string
print(f"\nb tag string : {b_str}")

print(b_str.next_sibling)

#if we change sibling to siblings then he return all value 