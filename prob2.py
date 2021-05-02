from bs4 import BeautifulSoup

with open("example.html" , "r") as file:
	soup = BeautifulSoup(file , "lxml")
	
# print(soup)
l = soup.find_all("div")
print(l)
data = [ a.string for a in l]
print(data)
# Outout : 

dataclass = [a["class"][0] for a in l]
print(dataclass)
