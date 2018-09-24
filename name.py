import requests
import bs4
import csv

#List to store data
genders = []
names = []
yomis = []

#Extract HTML
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

#Export list to CSV
with open('namelist.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for g in genders:
        writer.writerow(g)
    for n in names:
        writer.writerow(n)
    for y in yomis:
        writer.writerow(y)

#Genders are still in tag format. Want to label it as female, male.
#CSV is in a row but want to change it to columns.