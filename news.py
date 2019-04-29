'''load packages'''
import requests
from bs4 import BeautifulSoup
import pagescraper
import csv
sitelist=['http://www.nasdaq.com/symbol/atvi/news-headlines','http://www.nasdaq.com/symbol/gluu/news-headlines','http://www.nasdaq.com/symbol/gme/news-headlines','http://www.nasdaq.com/symbol/znga/news-headlines','http://www.nasdaq.com/symbol/ntdoy/news-headlines']

array1=[]

for i in range(5):

    array1.append([])

    html = requests.get(sitelist[i]).content



    '''convert html to BeautifulSoup object'''
    soup = BeautifulSoup(html , 'lxml')

    '''get list of all links on webpage'''
    links = soup.find_all('a')
    urls = [link.get('href') for link in links]
    urls = [url for url in urls if url is not None]


    '''Filter the list of urls to just the news articles'''
    news_urls = [url for url in urls if '/article/' in url]
    news_urls1 = [url for url in urls if 'https://www.nasdaq.com/article/activision-blizzard-searches-for-a-turnaround-in-2019-cm1136731' in url]



    for j in range(len(news_urls)):

            array1[i].append(news_urls[j])



###########end of the for loop for updating the array array1


##check the max length of a row cuz each row has different lengths yo

l=[]
for h in range(5):
    l.append(len(array1[h]))

m=max(l[0:4])


##fill the rows that dont have a length of 22 with []
for row in range(5):
    re=m-len(array1[row])
    for rest in range(re):
        array1[row].append(["n/a"])


print(array1)
with open("stocknews.csv","w",newline='')as mycsv:
    csvWriters=csv.writer(mycsv,delimiter=',')
    csvWriters.writerows(array1)





