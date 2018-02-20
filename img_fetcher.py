from bs4 import BeautifulSoup
import requests
import re
from urllib.request import urlopen,Request,urlretrieve
import os
#import cookielib
import json

def get_soup(url,header):
    return BeautifulSoup(urlopen(Request(url,headers=header)),'html.parser')

def img_fetch(query,DIR):
    query= query.split()
    query='+'.join(query)
    print (query)
    url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
    print (url)

    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
    }
    soup = get_soup(url,header)


    ActualImages=[]# contains the link for Large original images, type of  image
    for a in soup.find_all("div",{"class":"rg_meta"}):
        link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
        ActualImages.append((link,Type))

    print  ("there are total %d images" %len(ActualImages))
    for items in ActualImages:
        print(items)
    if not os.path.exists(DIR):
                os.mkdir(DIR)
    DIR = os.path.join(DIR, query.split()[0])

    if not os.path.exists(DIR):
                os.mkdir(DIR)
    ###print images
    for i , (img , Type) in enumerate( ActualImages):
        try:
            cntr = len([i for i in os.listdir(DIR)]) + 1
            print (cntr)
            imgdetails = urlretrieve(img,'%s/%s.%s'%(DIR,cntr,Type))
            print(imgdetails)
        except Exception as e:
            print ("could not load :%s "%img)
            print (e)
