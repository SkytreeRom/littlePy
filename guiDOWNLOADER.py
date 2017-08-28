from tkinter import *
from PIL import Image,ImageTk
def starCrawl():
    print('start')
def stopCrawl():
    print('stop')
if  __name__=='__main__':
    root=Tk()
    root.title('Multiple Images Downloader')
    root.geometry('800x600')
    root.resizable(width=False,height=False)
    Label(root,text='Multiple Images Downloader',font=("Arial",12)).pack(side=TOP)
    frameMain=Frame()
    frameMain.pack(side=TOP)

    # left frame
    framLeft=Frame(frameMain)
    Label(framLeft,text='Please input keyword:').grid(row=0,sticky=W)
    name=StringVar()
    nameEntry=Entry(framLeft,textvariable=name)
    Label(framLeft,text='Pleae input number:').grid(row=1,sticky=W)
    number=IntVar()
    numberEntry=Entry(framLeft,textvariable=number)
    nameEntry.grid(row=0,column=1)
    numberEntry.grid(row=1,column=1)
    framLeft.pack(side=LEFT)
    checkBaidu=IntVar()
    checkGoogle=IntVar()
    checkBtnBD=Checkbutton(framLeft,text='Baidu',variable=checkBaidu)
    checkBtnGOO=Checkbutton(framLeft,text='Google',variable=checkGoogle)
    checkBtnBD.grid(row=2,column=0)
    checkBtnGOO.grid(row=2,column=1)
    Button(framLeft,text='START',command=starCrawl).grid(row=3,column=0)
    Button(framLeft,text='STOP',command=stopCrawl).grid(row=3,column=1)



    # right frame
    framRight=Frame(frameMain)
    scrollbar = Scrollbar(framRight)
    scrollbar.pack(side=RIGHT,fill=Y)
    for i in range(10):
        img=ImageTk.PhotoImage(Image.open('cc.jpg').resize((100,100),Image.ANTIALIAS))
        Label(framRight,image=img).pack(side=TOP)

    framRight.pack(side=RIGHT)

    root.mainloop()


