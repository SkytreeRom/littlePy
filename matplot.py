import requests
import bs4
from bs4 import BeautifulSoup
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=5)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,'html.parser')
    i=0
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):#important
            i=i+1
            tds=tr.find_all('td')
            print(tds)
            ulist.append([i,tds[1].string,tds[2].string])

def printUnivList(ulist,num):
    print("{:^10}\t{:^10}\t{:^10}".format("排名","学校","得分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        # print(u)
        print("{0:^10}\t{1:{3}^10}\t{2:^10}".format(u[0],u[1],u[2],chr(12288)))
    print("Suc"+str(num))

def main():
    uinfo=[]
    url='http://zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)
if __name__ == '__main__':
    main()