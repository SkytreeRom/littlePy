from tkinter import *
if  __name__=='__main__':
    root=Tk()
    root.title('Multiple Images Downloader')
    # root.geometry('800x600')
    root.resizable(width=False,height=False)
    Label(root,text='Multiple Images Downloader',font=("Arial",12)).pack(side=TOP)
    frameMain=Frame()
    frameMain.pack(side=TOP)

    # left frame
    framLeft=Frame(frameMain)
    Label(framLeft,text='Please input keyword:').grid(row=0,sticky=W)
    name=vars()
    nameEntry=Entry(framLeft,textvariable=name)
    Label(framLeft,text='Pleae input number:').grid(row=1,sticky=W)
    number=vars()
    numberEntry=Entry(framLeft,textvariable=number)
    nameEntry.grid(row=0,column=1)
    numberEntry.grid(row=1,column=1)

    framLeft.pack(side=LEFT)


    # right frame
    framRight=Frame(frameMain)
    Label(framRight, text='Please input keyword:').pack()
    framRight.pack(side=RIGHT)
    root.mainloop()


