from bs4 import BeautifulSoup

with open("example.html") as fp:
   soup = BeautifulSoup(fp , 'lxml')

soup = BeautifulSoup("<html>data</html>" , "html.parser")
print(soup)	
# print(type(soup))

html = '''<b>tutorialspoint</b> <i>&web scraping &data science</i>'''
soup = BeautifulSoup(html, 'lxml')
# lxml pareser auto correct the format
# print(type(soup))
print(soup)
with open("example.html" , "a") as fp:
  fp.write(str(soup))