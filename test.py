test='ippr_z2C$qAzdH3FAzdH3Ft-0_z&e3Bevt42_z&e3Bv54AzdH3Fp6t4AzdH3F1uk91bbjuujkbwdvlldb1klnd09bnvlbdbbnmddAzdH3Fp6t4_z&e3B3r2'
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
if __name__ == '__main__':
    print(transURL(test))