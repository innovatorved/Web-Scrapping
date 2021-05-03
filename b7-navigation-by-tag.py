# python navigation-by-tag.py

html_doc = """<html><head><title>Tutorials Point</title></head>
<body>
<p class="title"><b>The Biggest Online Tutorials Library, It's all Free</b></p>
<p class="prog">Top 5 most used Programming Languages are:
<a href="https://www.tutorialspoint.com/java/java_overview.htm" class="prog" id="link1">Java</a>,
<a href="https://www.tutorialspoint.com/cprogramming/index.htm" class="prog" id="link2">C</a>,
<a href="https://www.tutorialspoint.com/python/index.htm" class="prog" id="link3">Python</a>,
<a href="https://www.tutorialspoint.com/javascript/javascript_overview.htm" class="prog" id="link4">JavaScript</a> and
<a href="https://www.tutorialspoint.com/ruby/index.htm" class="prog" id="link5">C</a>;
as per online survey.</p>
<p class="prog">Programming Languages</p>
<div>
<b>Hello i am b tag</b>
</div>
"""


from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc , "html.parser")

# lets extract tags
head = soup.head
print(f"head : {head}")
# print(head.contents)
title = soup.title
print(f"\nWeb Page Title : {title}")
# print(soup.prettify())
# extractb tag from body
b = soup.b
print(f"\nb tag : {b}")

b = soup.body.div.b
print(f"\nb tag : {b}")

bl = soup.find_all("b")
print(f"\nlist of all b tag : {bl}\n\n")

h = head.contents
print(f"\n{h}")

print(f"\n\n{head.contents[0].contents}")

#print(f"\n\n{soup.string}") # output : None
for x in head.contents[0].children:
	print(x)

print("\n\n")
"""
.descendants

The .descendants attribute allows you to iterate over all of a tag’s children, recursively −

its direct children and the children of its direct children and so on −
"""
l4 = (list(soup.descendants))
print(len(l4))
# print(l4[12])