import pandas as pd
import csv
import bs4
import requests
import time

pages = [str(i) for i in range(1,3)]

#Extract male name list
for page in pages:
    response = requests.get('https://b-name.jp/%E8%B5%A4%E3%81%A1%E3%82%83%E3%82%93%E5%90%8D%E5%89%8D%E8%BE%9E%E5%85%B8/m/%E3%81%82/?p=' + page)
    time.sleep(5)

    if response.status_code != 200:
        warn('Request: {}; Status code: {}'.format(requests, response.status_code))
    
    #Extract names and yomis
    page_html = bs4.BeautifulSoup(response.text, 'html.parser')
    cellnames = page_html.find_all(class_="cell-name")
    names = [c.get_text() for c in cellnames]
    cellyomis = page_html.find_all(class_="cell-yomi")
    yomis = [y.get_text() for y in cellyomis]

    #Put it in a chart
    namelist_m = pd.DataFrame({
        'name': names,
        'yomi': yomis,
    })
    namelist_m.to_csv("namelist_m.csv", mode="a")

#Extract female list
for page in pages:
    response = requests.get('https://b-name.jp/%E8%B5%A4%E3%81%A1%E3%82%83%E3%82%93%E5%90%8D%E5%89%8D%E8%BE%9E%E5%85%B8/f/%E3%81%82/?p=' + page)
    time.sleep(5)

    if response.status_code != 200:
        warn('Request: {}; Status code: {}'.format(requests, response.status_code))
    
    #Extract names and yomis
    page_html = bs4.BeautifulSoup(response.text, 'html.parser')
    cellnames = page_html.find_all(class_="cell-name")
    names = [c.get_text() for c in cellnames]
    cellyomis = page_html.find_all(class_="cell-yomi")
    yomis = [y.get_text() for y in cellyomis]

    #Put it in a chart
    namelist_f = pd.DataFrame({
        'name': names,
        'yomi': yomis,
    })
    namelist_f.to_csv("namelist_f.csv", mode="a")