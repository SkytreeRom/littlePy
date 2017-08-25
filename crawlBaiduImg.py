import requests
import  re
import traceback
def getHTML(url):
    try:
        head='Mozilla/5.0 '
        r=requests.get(url,headers={'User-Agent':head})
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        traceback.print_exc()


def parseDownloadLink(dList,html):

    tmpList=re.findall(r'"ObjURL":".+?"',html)
    # 目前的思路从原服务器下载的成功率很低
    for i in range(len(tmpList)):
        try:
            dList.append(eval(re.search(r'"http.+?"',tmpList[i]).group(0)))
        except:
            traceback.print_exc()
            continue

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