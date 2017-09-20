import re
import requests
import traceback
import os
import json


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

    for i in range(len(allspellList)):
        brand=eval(allspellList[i].split(':')[1])
        carUrl=carDetailUrlTemplate+brand+'/'
        carDetailUrl.append(carUrl)
    # branList=allspellList.split()
def parseDetailInfo(url):
    global carDetailInfo
    html=getUrl(url+r'/peizhi/')
    cartmp=re.findall('\[\[\[.*\]\]\]',html)
    # print(len(carInfo[0].split(r']],[['))
    # carInfo=carInfo[0].split(r']],[[')[0][1::]+']]'#获得的数据多一个[，少两个]]
    # print(carInfo)
    # print(carInfo[1])
    # 同一款车又有具体的很多车型，只选择网页提供的第一款进行数据爬取
    carInfo=eval(cartmp[0])#carInfo[0]中包含了全部的具体车型的全部信息
    tmpInfo=carInfo[0]
    # print(tmpInfo)
    #构建一个dict
    tmpDict={'车辆基础信息':tmpInfo[0],
             '基本信息':tmpInfo[1],
             '车体':tmpInfo[2],
             '发动机':tmpInfo[3],
             '变速箱':tmpInfo[4],
             '底盘制动':tmpInfo[5],
             '安全配置':tmpInfo[6],
             '车轮':tmpInfo[7],
             '行动辅助':tmpInfo[8],
             '门窗后镜':tmpInfo[9],
             '灯光':tmpInfo[10],
             '内部配置':tmpInfo[11],
             '座椅':tmpInfo[12],
             '娱乐通讯':tmpInfo[13],
             '空调冰箱':tmpInfo[15],
             }
    carName=url.split('/')[-2]
    carDetailInfo[carName]=tmpDict
    # print(carDetailInfo)






if __name__ == '__main__':
    carDetailUrl = []
    carDetailInfo={}
    if not os.path.exists('data.txt'): #不存在
        urlList = generateUrl(60)  # 生成x页的包含车辆整体信息的url
        for i in range(len(urlList)):
            parseUrl(urlList[i])#通过整体信息页面产生出每辆车详细信息的url
        print(len(carDetailUrl))
        with open('data.txt','w') as f:
            f.write(str(carDetailUrl))
            f.close()

    else:
        tmpCarList=[]
        with open('data.txt') as f:
            tmpCarList=f.read()
            f.close()
        carDetailUrl = tmpCarList[1:-1].split(',')#[1,-1]将[]两个符号去除
        for i in range(len(carDetailUrl)):
            try:
                parseDetailInfo(eval(carDetailUrl[i]))
                print(i,carDetailUrl[i])
            except:
                continue
        #所有车辆信息收集完毕后
        # parseDetailInfo('http://car.bitauto.com/baojun510/')
        with open('detail.json','w') as f:
            f.write(json.dumps(carDetailInfo))
            f.close()




