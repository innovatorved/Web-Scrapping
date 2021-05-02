# multi-valued-attributes.py
"""
Some of the HTML5 attributes can have multiple values. Most commonly used is the class-attribute which can have multiple CSS-values. Others include ‘rel’, ‘rev’, ‘headers’, ‘accesskey’ and ‘accept-charset’. The multi-valued attributes in beautiful soup are shown as list.
"""

from bs4 import BeautifulSoup

html = """
		<div class = "bold" id ="bold small">
		</div>
		<!--multi valur class -->
		<p class="bold small">
		</p>
"""
# print(html)
# class is multi value attribute soit extract in list
soup = BeautifulSoup(html, "lxml")
# if we pass xml at the place of lxml there is no multi-valued-attributes
print(f"Soup : {soup}\n type: {type(soup)}\n\n")

tagdiv = soup.div
tagp = soup.p

print(f"tagdiv : {tagdiv}\n{tagdiv['class']}\n")
print(f"tagp : {tagp}\n{tagp['class']}\n")

# if attribute is not muti value attribute it returb  string
#from id atttibute
# tagdiv contain id attribute
print(f"tagdiv['id'] : {tagdiv['id']} \n type : {type(tagdiv['id'])}\n")

# By using ‘get_attribute_list’, you get a value that is always a list, string, irrespective of whether it is a multi-valued or not.

# apply in id
idvalue = tagdiv.get_attribute_list("id")
print(f"idvalue : {idvalue}\n")

# NavigableString
'''
The navigablestring object is used to represent the contents of a tag. To access the contents, use “.string” with tag.'''
