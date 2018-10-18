import requests
from bs4 import BeautifulSoup
import random
import os
import csv
import chardet

class crawler_novel:
    def __init__(self):
        #variable
        self.url = 'https://www.101novel.com/ck101/355/257175.html'
        self.fileName = 'novel.csv'

    def download(self):
        my_headers = [
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
            "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
            'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
            "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
            "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
        ]
        headers = {'User-Agent': random.choice(my_headers)}
        try:
            with open(self.fileName, 'w', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['name', 'content'])
                while True:
                    r = requests.get(self.url, headers = headers)
                    r.encoding = 'big5'
                    if r.status_code == requests.codes.ok:
                        soup = BeautifulSoup(r.text, 'html.parser')
                        links = soup.find(id = 'thumb')
                        for link in links:
                            if link.text == '下一章':
                                nxtpage = link
                        ch_name = soup.find('h1').text
                        content = soup.find('p').text.replace('\xa0', '').replace('\n', '').replace('\x00','')
                        
                    #write file
                    data = [ch_name, content]
                    writer.writerow(data)
                    #last
                    if nxtpage['href'] == '/ck101/355/257226.html':
                        print('complete')
                        break
                    else:
                        print(nxtpage['href'])
                        self.url = 'https://www.101novel.com' + nxtpage['href']
        except Exception as e:
            print(e)

    def readCSV(self):
        with open(self.fileName, 'r', newline='', encoding='utf-8') as csvfile:
            rows = csv.DictReader(csvfile)
            for row in rows:
                print(row['name'])
                print(row['content'])

                
    
crawler_novel = crawler_novel()
#crawler_novel.download()
crawler_novel.readCSV()