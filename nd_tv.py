import csv,requests,json
from locale import DAY_1
from bs4 import BeautifulSoup
from pprint import pprint

url1=requests.get("https://www.ndtv.com/latest#pfrom=home-ndtv_mainnavgation")
soup=BeautifulSoup(url1.text,"html.parser")
a=[]
for i in range(1,9):
    d1=soup.find("div",class_="listng_pagntn clear").a['href']
    a.append(d1)


def nd_tv(a):
    # data={}
    all_pages=[]
    for i in range(len(a)):
        x=a[i][0:-1]
        y=x+str(i+1)
        all_data=[]
        question=requests.get(y)
        soup=BeautifulSoup(question.text,"html.parser")
        data1=soup.find("div",class_="lisingNews")
        data2=data1.find_all("div",class_="news_Itm")
        for i in data2:
            data={}
            try :
                tiles=i.find("h2",class_="newsHdng").get_text()
                data["title"]=tiles
                cont=i.find("p",class_="newsCont").get_text()
                data["content"]=cont
                writer=i.find("span",class_="posted-by").a.text
                data["writer"]=writer
                date=i.find("span",class_="posted-by").text
                p=date.split("|")
                g=p[1].split(",")
                j=g[0]+","+g[1][0:4]
                data["date"]=j
                all_data.append(data)    
            except:
                continue
        all_pages.append(all_data)
    with open("nd_tv.json","w") as p:
        json.dump(all_pages,p,indent=4)

nd_tv(a)
