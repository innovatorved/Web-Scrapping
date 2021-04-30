from bs4 import BeautifulSoup
import requests

url = "https://www.tutorialspoint.com/tutorialslibrary.htm"
main = "https://www.tutorialspoint.com"
req = requests.get(url)

soup = BeautifulSoup(req.text , "html.parser")
# print(soup)
# find all link avail in url
# ____.find_all("element") used for finding all specific element 
a_list = soup.find_all("a") 
print(type(soup))
# contain list of all a tags
link_list = []
a = "/"
for link  in a_list:
	# print(link)
	l = link.get("href")
	# print(l)
	if l != None:
		if a == l[0] : l=main+l
		link_list.append(l)

# print(link_list)
print(len(link_list))
link_list = list(set(link_list))
print(len(link_list))