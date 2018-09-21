import requests
from bs4 import BeautifulSoup

page = requests.get("https://b-name.jp/%E8%B5%A4%E3%81%A1%E3%82%83%E3%82%93%E5%90%8D%E5%89%8D%E8%BE%9E%E5%85%B8/m/%E3%81%82/?p=1")
soup = BeautifulSoup(page.content, 'html.parser')

#Extract all names
cellnames = soup.find_all(class_="cell-name")
names = [c.get_text() for c in cellnames]

#Extract all yomis
cellyomis = soup.find_all(class_="cell-yomi")
yomis = [y.get_text() for y in cellyomis]

import pandas as pd
namelist = pd.DataFrame({
    "name": names,
    "yomi": yomis
})
print(namelist)