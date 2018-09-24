import bs4
import requests
import time
import csv

#List to store data
genders = []
names = []
yomis = []

#Setting URL parameters
#Need to delete ぃ in between あ and い
pages = [str(i) for i in range(1,3)]
hiraganas = [chr(i) for i in range(ord('あ'), ord('い') + 1)]

#For every hiragana in the interval
for hiragana in hiraganas:

    #For every page in the interval
    for page in pages:
        
        #Make a get request
        response = requests.get('https://b-name.jp/%E8%B5%A4%E3%81%A1%E3%82%83%E3%82%93%E5%90%8D%E5%89%8D%E8%BE%9E%E5%85%B8/all/' + hiragana + '/?p=' + page)
        
        #Pause the loop
        time.sleep(2)

        #Throw a warning for non-200 status codes
        if response.status_code != 200:
            warn('Request: {}; Status code: {}'.format(requests, response.status_code))
        
        #Parse the content of the request with BeautifulSoup
        page_html = bs4.BeautifulSoup(response.text, 'html.parser')

        #Extract namelist
        namelist = page_html.find(class_="namelist")

        #Scrape the genders
        cellgenders = namelist.find_all(class_=["icon-woman","icon-man"])
        genders.append(cellgenders)
        #print(genders)

        #Scrape the names
        cellnames = namelist.find_all(class_="cell-name")
        name = [n.get_text() for n in cellnames]
        names.append(name)
        #print(names)

        #Scrape the yomis
        cellyomis = namelist.find_all(class_="cell-yomi")
        yomi = [y.get_text() for y in cellyomis]
        yomis.append(yomi)
        #print(yomis)

#Export to CSV
with open('namelist.csv', 'w') as f:
    writer = csv.writer(f)
    for g in genders:
        writer.writerow(g)
    for n in names:
        writer.writerow(n)
    for y in yomis:
        writer.writerow(y)

#Genders are still in tag format. Want to label it as female, male.
#CSV is in a row but want to change it to columns.