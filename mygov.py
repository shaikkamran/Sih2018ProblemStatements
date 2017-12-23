# Scrapes ALL The Problem Statements Of Smart India Hackathon 2018  from https://innovate.mygov.in/sih2018/ site.

from bs4 import BeautifulSoup

import requests
url="https://innovate.mygov.in/sih2018/"
reqfile = requests.get(url)
soup1 = BeautifulSoup(reqfile.content,"html.parser")
#Find all the links in the myGov Site 

links=soup1.find_all('div',{'class':"thumbnail"})

for newurl in links:
    reqfile1= requests.get(newurl.find('a')['href'])
    soup=BeautifulSoup(reqfile1.content,"html.parser")
    
    
    search=soup.find_all('div',{'class':"search-by"})
    content=soup.find_all('div',{'class':"description"})
    problem_list=problem_list=soup.find_all('div',{'class':"head-part"})

    for i in search:
        print(i.text)

    print("\n\n")
    cnt=0

    for i,j in zip(problem_list,content):
        cnt+=1
        print(cnt,end="\t\t")
        print(i.a.text)
        print()
        print(j.p.text)
        print("\n\n")


    print("\n\n\n\n\n\n")
        
    

    
