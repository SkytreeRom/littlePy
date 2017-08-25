import requests

if __name__ == '__main__':
    r=requests.get('http:\/\/pic.chinadaily.com.cn\/img\/attachement\/jpg\/site1\/20151010\/448a5bd66b2f1782c88d20.jpg'.replace('\\',''))
    r.encoding=r.apparent_encoding
    with open('x.jpg','wb') as f:
        f.write(r.content)
        f.close()
