import requests
import traceback
from bs4 import BeautifulSoup
import re
def getHTML(url,code='utf-8'):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=code
        return r.text
    except:
        return ""
def getStockList(lst,stockUrl):
    html=getHTML(stockUrl,'GB2312')
    soup=BeautifulSoup(html,'html.parser')
    a=soup.find_all('a')
    for i in a:
        try:
            href=i.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}',href)[0])
        except:
            continue
def getStockInfo(lst,stockUrl,fpath):
    count=0
    for stock in lst:
        url=stockUrl+stock+'.html'
        html=getHTML(url)
        try:
            if html=="":
                continue
            infoDict={}
            soup=BeautifulSoup(html,'html.parser')
            stockInfo=soup.find('div',attrs={'class':'stock-bets'})

            name=stockInfo.find(attrs={'class':'bets-name'})
            infoDict.update({'股票名称':name.text.split()[0]})
            keyList=stockInfo.find_all('dt')
            valueList=stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key=keyList[i].text
                value=valueList[i].text
                infoDict.update({key:value})
            with open(fpath,'a',encoding='utf-8') as f:
                f.write(str(infoDict)+'\n')
                count=count+1
                print('\r当前进度：{:.2f}%'.format(count*100/len(lst)),end=' ')
        except:
            count = count + 1
            print('\r当前进度：{:.2f}%'.format(count * 100 / len(lst)), end=' ')
            traceback.print_exc()
            continue
    pass
if __name__ == '__main__':
    stock_list_url='http://quote.eastmoney.com/stocklist.html'
    stock_info_url='https://gupiao.baidu.com/stock/'
    output_file='./data/BaiduStockInfo.txt'
    slist=[]
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url,output_file)