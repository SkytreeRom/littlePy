from bs4 import BeautifulSoup
import requests
import re


def getHtml(url):
    try:
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1'}
        r = requests.get(url, 'html.parser', headers=head)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def parseHtml(ilist, html):
    try:
        pl = re.findall(r'\"view_price\"\:\"\d*\.\d*\"', html)
        tl = re.findall(r'\"raw_title\"\:\".+?\"', html)  # 此处使用最小匹配，否则会不成功
        for i in range(len(pl)):
            price = eval(pl[i].split(':')[1])
            title = eval(tl[i].split(':')[1])
            ilist.append([title, price])
    except:
        print("页面查找信息失败")

def printList(ili):
    tpl='{0:^4}\t{1:^8}\t{2:<20}'
    print(tpl.format('序号','价格','名称'))
    for i in range(len(ili)):
        print(tpl.format(i+1,ili[i][1],ili[i][0]))


if __name__ == '__main__':
    urlTemplate = 'https://s.taobao.com/search?q={0}&s={1}'
    name = input('请输入爬取商品名称:\n')
    total = input('请输入爬取页面的数量:\n')
    ilist = []
    for i in range(int(total)):
        try:
            url = urlTemplate.format(name, str(44 * i))
            html = getHtml(url)
            parseHtml(ilist, html)
            printList(ilist)
        except:
            continue
