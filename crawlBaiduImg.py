import requests
import  re
import traceback
def getHTML(url):
    try:
        head='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 '
        r=requests.get(url,headers={'User-Agent':head})
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        traceback.print_exc()
def transURL(originURL):
    transDict={'w':'a','k':'b','v':'c','1':'d','j':'e','u':'f','2':'g','i':'h','t':'i','3':'j','h':'k','s':'l','4':'m',
               'g':'n','5':'o','r':'p','q':'q','6':'r','f':'s','p':'t','7':'u','e':'v','o':'w','8':'1','d':'2','n':'3',
               '9':'4','c':'5','m':'6','0':'7','b':'8','l':'9','a':'0',':':':','.':'.','/':'/','-':'-'}
    newURL=''
    originURL=originURL.replace('_z2C$q',':')
    originURL=originURL.replace('_z&e3B','.')
    originURL=originURL.replace('AzdH3F',r'/')
    originURL = originURL.lower()
    print(originURL)
    for i in originURL:
        newURL=newURL+transDict[i]
    return newURL

def parseDownloadLink(dList,html):

    tmpList=re.findall(r'"ObjURL":".+?"',html)
    # 目前的思路从原服务器下载的成功率很低
    for i in range(len(tmpList)):
        try:
            dList.append(eval(re.search(r'"http.+?"',tmpList[i]).group(0)))
        except:
            traceback.print_exc()
            continue
def parseJsonDownloadLink():
    pass

def saveImg(dList,fpath):
    for i in range(len(dList)):
        try:

            r=requests.get(dList[i].replace('\\',''),timeout=2)
            with open(fpath+str(i)+'.jpg','wb') as f:
                f.write(r.content)
                f.close()
                print('当前完成第{}个'.format(i),dList[i].replace('\\', ''))
        except:
            traceback.print_exc()
if __name__ == '__main__':
    fpath='./data/'
    url='https://image.baidu.com/search/index?tn=baiduimage&word='
    dList=[]
    searchName=input('请输入图像名称：\n')
    html=getHTML(url+searchName)
    parseDownloadLink(dList,html)
    saveImg(dList,fpath)