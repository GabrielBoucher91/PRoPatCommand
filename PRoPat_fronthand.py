#########################################################################################
#                                                                                       #
#Fronthand module of the software									                    #
#                                                                                       #
#                                                                                       #
#Author: Gabriel Boucher                                                                #
#                                                                                       #
#########################################################################################

import tkinter as tk


class Application(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):
        #Main frame of the application
        self.parent.title("PRoPat Command Software")
        self.pack(fill=tk.BOTH, expand=1)

        #Frames to layout the application
        bottomcolor='teal'
        bottomframe = tk.Frame(self,relief='raised',borderwidth=1,background=bottomcolor)
        bottomframe.pack(side=tk.BOTTOM,fill=tk.X)


        rightcolor='grey'
        rightframe=tk.Frame(self,relief='raised',borderwidth=1,background=rightcolor)
        rightframe.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)

        leftcolor='grey'
        leftframe=tk.Frame(self,relief='raised',borderwidth=1,background=leftcolor)
        leftframe.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)



        #Bottom
        self.comlabelvar=tk.StringVar()
        comlabel=tk.Label(bottomframe,text='COM',background=bottomcolor,textvariable=self.comlabelvar)
        comlabel.pack(side=tk.LEFT,padx=5,pady=5)

        portentryvar=tk.StringVar()
        portentryvar.set("1")
        portentry=tk.Entry(bottomframe,width=7,textvariable=portentryvar)
        portentry.pack(side=tk.LEFT,padx=15,pady=5)


        self.okbutton=tk.Button(bottomframe,text='CONNECT')
        self.okbutton.pack(side=tk.LEFT)

        quitButton = tk.Button(bottomframe,text='DISCONNECT',command=self.quit)
        quitButton.pack(side=tk.LEFT, padx=15, pady=5)

        #Right
        Rightlabel=tk.Label(rightframe,text='PID Management',background=rightcolor,font=15)
        Rightlabel.pack(side=tk.TOP)

        righttopframe1color='grey'
        righttopframe1=tk.Frame(rightframe,background=righttopframe1color)
        righttopframe1.pack(side=tk.TOP)

        righttopframe2=tk.Frame(rightframe,background=righttopframe1color)
        righttopframe2.pack(side=tk.TOP,pady=5)

        #Righttopframe1
        kpxlabel=tk.Label(righttopframe1,text='Kpx',background=righttopframe1color)
        kpxlabel.grid(row=0,column=0,padx=5,pady=3)

        self.kpxentryvar=tk.StringVar()
        kpxentry=tk.Entry(righttopframe1,width=10,textvariable=self.kpxentryvar)
        kpxentry.grid(row=0,column=1,padx=5,pady=3)

        kpylabel=tk.Label(righttopframe1,text='Kpy',background=righttopframe1color)
        kpylabel.grid(row=0,column=2,padx=5,pady=3)

        self.kpyentryvar=tk.StringVar()
        kpyentry=tk.Entry(righttopframe1,width=10,textvariable=self.kpyentryvar)
        kpyentry.grid(row=0,column=3,padx=5,pady=3)

        kpzlabel=tk.Label(righttopframe1,text='Kpz',background=righttopframe1color)
        kpzlabel.grid(row=0,column=4,padx=5,pady=3)

        self.kpzentryvar=tk.StringVar()
        kpzentry=tk.Entry(righttopframe1,width=10,textvariable=self.kpzentryvar)
        kpzentry.grid(row=0,column=5,padx=5,pady=3)


        kdxlabel=tk.Label(righttopframe1,text='Kdx',background=righttopframe1color)
        kdxlabel.grid(row=1,column=0,padx=5,pady=3)

        self.kdxentryvar=tk.StringVar()
        kdxentry=tk.Entry(righttopframe1,width=10,textvariable=self.kdxentryvar)
        kdxentry.grid(row=1,column=1,padx=5,pady=3)

        kdylabel=tk.Label(righttopframe1,text='Kdy',background=righttopframe1color)
        kdylabel.grid(row=1,column=2,padx=5,pady=3)

        self.kdyentryvar=tk.StringVar()
        kdyentry=tk.Entry(righttopframe1,width=10,textvariable=self.kdyentryvar)
        kdyentry.grid(row=1,column=3,padx=5,pady=3)

        kdzlabel=tk.Label(righttopframe1,text='Kdz',background=righttopframe1color)
        kdzlabel.grid(row=1,column=4,padx=5,pady=3)

        self.kdzentryvar=tk.StringVar()
        kdzentry=tk.Entry(righttopframe1,width=10,textvariable=self.kdzentryvar)
        kdzentry.grid(row=1,column=5,padx=5,pady=3)


        kixlabel=tk.Label(righttopframe1,text='Kix',background=righttopframe1color)
        kixlabel.grid(row=2,column=0,padx=5,pady=3)

        self.kixentryvar=tk.StringVar()
        kixentry=tk.Entry(righttopframe1,width=10,textvariable=self.kixentryvar)
        kixentry.grid(row=2,column=1,padx=5,pady=3)

        kiylabel=tk.Label(righttopframe1,text='Kiy',background=righttopframe1color)
        kiylabel.grid(row=2,column=2,padx=5,pady=3)

        self.kiyentryvar=tk.StringVar()
        kiyentry=tk.Entry(righttopframe1,width=10,textvariable=self.kiyentryvar)
        kiyentry.grid(row=2,column=3,padx=5,pady=3)

        kizlabel=tk.Label(righttopframe1,text='Kiz',background=righttopframe1color)
        kizlabel.grid(row=2,column=4,padx=5,pady=3)

        self.kizentryvar=tk.StringVar()
        kizentry=tk.Entry(righttopframe1,width=10,textvariable=self.kizentryvar)
        kizentry.grid(row=2,column=5,padx=5,pady=3)

        #righttopframe2
        sendKvaluesbutton=tk.Button(righttopframe2,text='Send K values',background='white')
        sendKvaluesbutton.grid(row=0,column=0,padx=5,pady=5)

        readKvaluesbutton=tk.Button(righttopframe2,text='Read K values',background='white')
        readKvaluesbutton.grid(row=0,column=1,padx=5,pady=5)


        #Left
        lefttopcolor='grey'
        lefttopframe=tk.Frame(leftframe,relief='raised',borderwidth=1,background=lefttopcolor)
        lefttopframe.pack(side=tk.TOP,fill=tk.BOTH,expand=False)

        leftbotcolor='green'
        leftbotframe=tk.Frame(leftframe,relief='raised',borderwidth=1,background=leftbotcolor)
        leftbotframe.pack(side=tk.TOP,fill=tk.BOTH,expand=True)

        #Lefttopframe
        leftlabel=tk.Label(lefttopframe,text='Axis Management',background=lefttopcolor,font=15)
        leftlabel.pack(side=tk.TOP)

        lefttopframe2=tk.Frame(lefttopframe,background=lefttopcolor)
        lefttopframe2.pack(side=tk.BOTTOM)

        clearxbuttoncolor='white'
        clearxbutton=tk.Button(lefttopframe2,text='Clear X',background=clearxbuttoncolor)
        clearxbutton.grid(row=0,column=0,padx=10,pady=5)

        clearybuttoncolor='white'
        clearybutton=tk.Button(lefttopframe2,text='Clear Y',background=clearybuttoncolor)
        clearybutton.grid(row=0,column=1,padx=10,pady=5)

        clearzbuttoncolor='white'
        clearzbutton=tk.Button(lefttopframe2,text='Clear Z',background=clearzbuttoncolor)
        clearzbutton.grid(row=0,column=2,padx=10,pady=5)

        clearFFbuttoncolor='white'
        clearFFbutton=tk.Button(lefttopframe2,text='Clear FF',background=clearFFbuttoncolor)
        clearFFbutton.grid(row=0,column=3,padx=10,pady=5)

        self.importxbuttoncolor='white'
        importxbutton=tk.Button(lefttopframe2,text='Import X',background=self.importxbuttoncolor)
        importxbutton.grid(row=1,column=0,padx=10,pady=5)

        self.importybuttoncolor='white'
        importybutton=tk.Button(lefttopframe2,text='Import X',background=self.importybuttoncolor)
        importybutton.grid(row=1,column=1,padx=10,pady=5)

        self.importzbuttoncolor='white'
        importzbutton=tk.Button(lefttopframe2,text='Import X',background=self.importzbuttoncolor)
        importzbutton.grid(row=1,column=2,padx=10,pady=5)

        self.importFFbuttoncolor='white'
        importFFbutton=tk.Button(lefttopframe2,text='Import X',background=self.importFFbuttoncolor)
        importFFbutton.grid(row=1,column=3,padx=10,pady=5)

        clearimportbuttoncolor='white'
        clearimportbutton=tk.Button(lefttopframe2,text='Clear Import',background=clearimportbuttoncolor)
        clearimportbutton.grid(row=3,column=0,columnspan=2,padx=10,pady=5)

        self.downloadAxisbuttoncolor='white'
        downloadAxisbutton=tk.Button(lefttopframe2,text='Download Axis',background=self.downloadAxisbuttoncolor)
        downloadAxisbutton.grid(row=3,column=2,columnspan=2,padx=10,pady=5)

        #Leftbotframe
        leftbotlabel=tk.Label(leftbotframe,text='Data Acquisition',background=leftbotcolor,font=15)
        leftbotlabel.pack(side=tk.TOP)





def mainWindow():
    root = tk.Tk()
    root.geometry("1000x500+200+200")
    app = Application(root)
    return(app,root)