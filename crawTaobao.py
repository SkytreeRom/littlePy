from bs4 import BeautifulSoup
import requests


def getHtml(url):
    pass


def parseHtml(ili, html):
    pass


def printList(ili):
    pass

if __name__ == '__main__':
    urlTemplate = 'https://s.taobao.com/search?q={0}&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170819&bcoffset=1&ntoffset=1&p4ppushleft=1%2C48&s={1}'
    name = input('请输入爬取商品名称:\n')
    total=input('请输入爬取页面的数量:\n')
    for i in range(1,int(total)+1):
        print(i)

