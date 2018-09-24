import requests
import bs4

#List to store data
genders = []
names = []
yomis = []

page = requests.get("https://b-name.jp/%E8%B5%A4%E3%81%A1%E3%82%83%E3%82%93%E5%90%8D%E5%89%8D%E8%BE%9E%E5%85%B8/all/%E3%81%82/?p=1")
page_html = bs4.BeautifulSoup(page.content, 'html.parser')

#Extract namelist
namelist = page_html.find(class_="namelist")
#print(namelist)

#Extract all genders
cellgenders = namelist.find_all(class_=["icon-woman","icon-man"])
genders.append(cellgenders)

#Extract all names
cellnames = namelist.find_all(class_="cell-name")
name = [n.get_text() for n in cellnames]
names.append(name)

#Extract all yomis
cellyomis = namelist.find_all(class_="cell-yomi")
yomi = [y.get_text() for y in cellyomis]
yomis.append(yomi)

print(genders)
print(names)
print(yomis)