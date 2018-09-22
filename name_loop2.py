import bs4
import requests
import time

#List to store data
names = []
yomis = []

#Setting URL parameters
pages = [str(i) for i in range(1,3)]
hiraganas = [chr(i) for i in range(ord('あ'), ord('ん') + 1)]

#For every hiragana in the interval あ to ん
for hiragana in hiraganas:

    #For every page in the interval 0-2
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

        #Scrape the genders
        
        #Scrape the names
        cellnames = page_html.find_all(class_="cell-name")
        name = [c.get_text() for c in cellnames]
        names.append(name)
        
        #Scrape the yomis
        cellyomis = page_html.find_all(class_="cell-yomi")
        yomi = [y.get_text() for y in cellyomis]
        yomis.append(yomi)

        #Print the lists
        print(names)
        print(yomis)

        #Export to CSV