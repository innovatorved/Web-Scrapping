# python b8-stripped_strings.py

html = """<html><head><title>Tutorials Point</title></head>
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
soup = BeautifulSoup(html , "html.parser")
print(type(soup))
# print(list())
"""
.strings and stripped_strings

If there’s more than one thing inside a tag, you can still look at just the strings. Use the .strings generator −

.string use for extract data from single element
.string or .stripped_strings extract data from all tag avail in <class 'bs4.BeautifulSoup'>
but .stripped_strings To remove extra whitespace, use .stripped_strings generator −
"""
for x in soup.stripped_strings:
	print(repr(x))

print(f"\n\n{list(soup.strings)}")