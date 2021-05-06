from bs4 import *
import requests as rq
import os


url1 = 'https://www.gettyimages.in/photos/driving-without-mask?page='
url2 = '&phrase=driving%20without%20mask&sort=mostpopular'

url_list=[]
Links = []

for i in range(1,30):
    full_url = url1+str(i)+url2
    url_list.append(full_url)

for lst in url_list:
    r2 = rq.get(lst)
    soup = BeautifulSoup(r2.text, 'html.parser')

    x=soup.select('img[src^="https://media.gettyimages.com/photos/"]')

    for img in x:
        Links.append(img['src'])
    print(len(Links))



for index, img_link in enumerate(Links):
   if i <= len(Links):
       img_data = rq.get(img_link).content
       with open("Non_Masked_Drivers/" + str(index + 1) + '.jpg', 'wb+') as f:
           f.write(img_data)
           i += 1



