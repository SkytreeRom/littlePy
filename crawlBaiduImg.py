import requests
import  re
import traceback
import math

succesNumber = 1
def getHTML(url):
    try:
        head='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
        r=requests.get(url,headers={'User-Agent':head})
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        traceback.print_exc()
def transURL(originURL):
    transDict={'w':'a','k':'b','v':'c','1':'d','j':'e','u':'f','2':'g','i':'h','t':'i','3':'j','h':'k','s':'l','4':'m',
               'g':'n','5':'o','r':'p','q':'q','6':'r','f':'s','p':'t','7':'u','e':'v','o':'w','8':'1','d':'2','n':'3',
               '9':'4','c':'5','m':'6','0':'7','b':'8','l':'9','a':'0'}
    newURL=''
    originURL=originURL.replace('_z2C$q',':')
    originURL=originURL.replace('_z&e3B','.')
    originURL=originURL.replace('AzdH3F',r'/')
    # originURL = originURL.lower()
    # print(originURL)
    for i in originURL:
        if i in transDict:
            newURL=newURL+transDict[i]
        else:
            newURL=newURL+i
    return newURL

def parseDownloadLink(dList,html):

    tmpList=re.findall(r'"objURL":".+?"',html)
    # 目前的思路从原服务器下载的成功率很低
    for i in range(len(tmpList)):
        try:
            dList.append(eval(re.search(r'"ippr.+?"',tmpList[i]).group(0)))
        except:
            traceback.print_exc()
            continue


def saveImg(dList,fpath):
    global succesNumber
    for i in range(len(dList)):
        try:
            r=requests.get(transURL(dList[i]),timeout=10)
            with open(fpath+str(succesNumber)+'.jpg','wb') as f:
                f.write(r.content)
                f.close()
                print('当前完成第{}个'.format(succesNumber),transURL(dList[i]))
                succesNumber = succesNumber + 1
        except:
            traceback.print_exc()
            continue
if __name__ == '__main__':
    fpath='./data/'
    url='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={0}&cl=&lm=&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word={0}&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&pn={1}&rn=30&gsm=1e&1503712018315='
    dList=[]
    searchName=input('请输入图像名称：\n')
    number=input('请输入下载图像数量（30的整数倍）:\n')
    for i in range(math.ceil(int(number)/30)):
        html=getHTML(url.format(searchName,str(i*30)))
        # print(url.format(searchName,str(i*30)))
        parseDownloadLink(dList,html)
        saveImg(dList,fpath)