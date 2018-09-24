import bs4
import requests
import time
import csv
import pandas as pd

#List to store data
genders = []
names = []
yomis = []

#Setting URL parameters
pages = [str(i) for i in range(1,3)]
hiraganas = [chr(i) for i in range(ord('あ'), ord('い') + 1)]

#For every hiragana in the interval
for hiragana in hiraganas:

    #For every page in the interval
    for page in pages:
        
        #Make a get request
        response = requests.get('https://b-name.jp/%E8%B5%A4%E3%81%A1%E3%82%83%E3%82%93%E5%90%8D%E5%89%8D%E8%BE%9E%E5%85%B8/all/' + hiragana + '/?p=' + page + '&t=s&mode=1')
        
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
        cellgenders = [c.get('class')[0] for c in cellgenders]
        for c in cellgenders:
            if c == "icon-woman":
                genders.append("female")
            elif c == "icon-man":
                genders.append("male")

        #Scrape the names
        cellnames = namelist.find_all(class_="cell-name")
        name = [n.get_text() for n in cellnames]
        names.extend(name)
        #print(names)

        #Scrape the yomis
        cellyomis = namelist.find_all(class_="cell-yomi")
        yomi = [y.get_text() for y in cellyomis]
        yomis.extend(yomi)
        #print(yomis)

#Consolidate into result list
result = []
for i in range(0, len(names)):
    a = genders[i]
    b = names[i]
    c = yomis[i]
    result.append([a, b, c])
print(result)

#Export list to CSV
with open('namelist_db.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)