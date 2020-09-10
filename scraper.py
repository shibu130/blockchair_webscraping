# beautiful soup
from bs4 import BeautifulSoup
import requests as req
from time import perf_counter

t1=perf_counter()

url="url here"

page=req.get(url)


soup = BeautifulSoup(page.content, 'html.parser')

a=soup.find('bdi')

for i in a.find_all('span',class_='grey'):
    print(float(i.contents[0]))
    break


t2=perf_counter()


print("{0} time elaspsed".format(str(t2-t1)))
# print(a)
