from PIL import Image
import numpy as np
from scipy import fftpack
import os
import csv
def dct2(a):
    return fftpack.dct( fftpack.dct( a, axis=0, norm='ortho' ), axis=1, norm='ortho' )
def idct2(a):
    return fftpack.idct( fftpack.idct( a, axis=0 , norm='ortho'), axis=1 , norm='ortho')
def getHash(filename):
    im=Image.open(filename)
    tmp=im.resize((32,32),Image.ANTIALIAS).convert('L')
    dctImg=np.abs(dct2(np.array(tmp)))[0:8,0:8]
    meanDct=dctImg.mean()
    outHash=np.zeros((8,8),dtype='uint8')
    for i in range(8):
        for j in range(8):
            if dctImg[i][j]>meanDct:
                outHash[i][j]=1
    # outHash.resize(1,64)
    return outHash.reshape(1,64)

if __name__=='__main__':
    path='./data/'
    nameList=os.listdir(path)
    hashList=[]
    outList=[]
    with open( 'hash.csv', 'w',newline='') as f:#去除空行
        w = csv.writer(f)
        for i in range(len(nameList)):
            hashValue=getHash(path+nameList[i]).tolist()
            # outList.append([nameList[i],hashValue[0]])
            w.writerow([nameList[i], str(hashValue[0])])
            # w.writerow(['xx','xx'])
        print('FINISHED')
        f.close()

