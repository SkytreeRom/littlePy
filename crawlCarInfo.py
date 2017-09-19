import re
import requests
import traceback


def generateUrl(page):
    urlList = []
    urlTemplate = 'http://select.car.yiche.com/selectcartool/searchresult?page={}&external=Car&callback=jsonpCallback'
    for i in range(page):
        urlList.append(urlTemplate.format(i + 1))
    return urlList


def getUrl(url):
    try:
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        return r.text
    except:
        traceback.print_exc()
        return ''


def parseUrl(url):
    global carDetailUrl
    carDetailUrlTemplate='http://car.bitauto.com/'
    html=getUrl(url)
    allspellList=re.findall(r'"AllSpell":".*?"',html)
    a=1
    for i in range(len(allspellList)):
        brand=eval(allspellList[i].split(':')[1])
        carUrl=carDetailUrlTemplate+brand+'/'
        carDetailUrl.append(carUrl)
    # branList=allspellList.split()

def test():
    try:
        r = requests.get(
            url='http://select.car.yiche.com/selectcartool/searchresult?page=2&external=Car&callback=jsonpCallback')
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        return r.text
    except:
        traceback.print_exc()
        return ''


if __name__ == '__main__':
    carDetailUrl = []
    urlList = generateUrl(60)  # 生成x页的包含车辆整体信息的url
    for i in range(len(urlList)):
        parseUrl(urlList[i])#通过整体信息页面产生出每辆车详细信息的url
    print(len(carDetailUrl))
    with open('data.txt','w') as f:
        f.write(str(carDetailUrl))
        f.close()

