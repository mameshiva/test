import requests
import pandas as pd
import csv
from bs4 import BeautifulSoup
from requests import get
from IPython.core.display import clear_output
from time import sleep
from random import randint
from time import time

pages = [str(i) for i in range(1,3)]

start_time = time()
requests = 0

#Extract male name list
for page in pages:
    response = get('https://b-name.jp/%E8%B5%A4%E3%81%A1%E3%82%83%E3%82%93%E5%90%8D%E5%89%8D%E8%BE%9E%E5%85%B8/m/%E3%81%82/?p=' + page)
    sleep(randint(1,3))
    requests += 1
    clear_output(wait = True)

    if response.status_code != 200:
            warn('Request: {}; Status code: {}'.format(requests, response.status_code))
    
    #Extract names and yomis
    page_html = BeautifulSoup(response.text, 'html.parser')
    cellnames = page_html.find_all(class_="cell-name")
    names = [c.get_text() for c in cellnames]
    cellyomis = page_html.find_all(class_="cell-yomi")
    yomis = [y.get_text() for y in cellyomis]

    #Put it in a chart
    namelist_m = pd.DataFrame({
        'name': names,
        'yomi': yomis,
    })
    namelist_m.to_csv("namelist_m.csv")

#Extract female list
for page in pages:
    response = get('https://b-name.jp/%E8%B5%A4%E3%81%A1%E3%82%83%E3%82%93%E5%90%8D%E5%89%8D%E8%BE%9E%E5%85%B8/f/%E3%81%82/?p=' + page)
    sleep(randint(1,3))
    requests += 1
    clear_output(wait = True)

    if response.status_code != 200:
            warn('Request: {}; Status code: {}'.format(requests, response.status_code))
    
    #Extract names and yomis
    page_html = BeautifulSoup(response.text, 'html.parser')
    cellnames = page_html.find_all(class_="cell-name")
    names = [c.get_text() for c in cellnames]
    cellyomis = page_html.find_all(class_="cell-yomi")
    yomis = [y.get_text() for y in cellyomis]

    #Put it in a chart
    namelist_f = pd.DataFrame({
        'name': names,
        'yomi': yomis,
    })
    namelist_f.to_csv("namelist_f.csv")