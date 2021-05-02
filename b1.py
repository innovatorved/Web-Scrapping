from bs4 import BeautifulSoup
import requests

url = "https://www.tutorialspoint.com/tutorialslibrary.htm"
req = requests.get(url)
# print(req)
# print(req.content)
# extract title from website
soup = BeautifulSoup(req.text, "html.parser") # change in to html
# print(soup)
# print any element from html always print first element
print(soup.title) # print title