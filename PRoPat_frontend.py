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


        rightcolor='light grey'
        rightframe=tk.Frame(self,relief='raised',borderwidth=1,background=rightcolor)
        rightframe.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)

        leftcolor='light grey'
        leftframe=tk.Frame(self,relief='raised',borderwidth=1,background=leftcolor)
        leftframe.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)



        #Bottom
        comlabel=tk.Label(bottomframe,text='COM',background=bottomcolor)
        comlabel.pack(side=tk.LEFT,padx=5,pady=5)

        self.portentryvar=tk.StringVar()
        self.portentryvar.set("1")
        portentry=tk.Entry(bottomframe,width=7,textvariable=self.portentryvar)
        portentry.pack(side=tk.LEFT,padx=15,pady=5)


        self.okbutton=tk.Button(bottomframe,text='CONNECT')
        self.okbutton.pack(side=tk.LEFT)

        self.quitButton = tk.Button(bottomframe,text='DISCONNECT',command=self.quit)
        self.quitButton.pack(side=tk.LEFT, padx=15, pady=5)

        #Right
        Rightlabel=tk.Label(rightframe,text='PID Management',background=rightcolor,font=15)
        Rightlabel.pack(side=tk.TOP)

        righttopframe1color='light grey'
        righttopframe1=tk.Frame(rightframe,background=righttopframe1color)
        righttopframe1.pack(side=tk.TOP)

        righttopframe2=tk.Frame(rightframe,background=righttopframe1color)
        righttopframe2.pack(side=tk.TOP,pady=5)

        trajectorylabel=tk.Label(rightframe,text='Trajectory Control',background=rightcolor,font=15)
        trajectorylabel.pack(side=tk.TOP)

        righttopframe3=tk.Frame(rightframe,background=righttopframe1color)
        righttopframe3.pack(side=tk.TOP,pady=5)

        #Righttopframe1
        kpxlabel=tk.Label(righttopframe1,text='Kpx',background=righttopframe1color)
        kpxlabel.grid(row=0,column=0,padx=5,pady=3)

        self.kpxentryvar=tk.StringVar()
        self.kpxentry=tk.Entry(righttopframe1,width=10,textvariable=self.kpxentryvar)
        self.kpxentry.grid(row=0,column=1,padx=5,pady=3)

        kpylabel=tk.Label(righttopframe1,text='Kpy',background=righttopframe1color)
        kpylabel.grid(row=0,column=2,padx=5,pady=3)

        self.kpyentryvar=tk.StringVar()
        self.kpyentry=tk.Entry(righttopframe1,width=10,textvariable=self.kpyentryvar)
        self.kpyentry.grid(row=0,column=3,padx=5,pady=3)

        kpzlabel=tk.Label(righttopframe1,text='Kpz',background=righttopframe1color)
        kpzlabel.grid(row=0,column=4,padx=5,pady=3)

        self.kpzentryvar=tk.StringVar()
        self.kpzentry=tk.Entry(righttopframe1,width=10,textvariable=self.kpzentryvar)
        self.kpzentry.grid(row=0,column=5,padx=5,pady=3)


        kdxlabel=tk.Label(righttopframe1,text='Kdx',background=righttopframe1color)
        kdxlabel.grid(row=1,column=0,padx=5,pady=3)

        self.kdxentryvar=tk.StringVar()
        self.kdxentry=tk.Entry(righttopframe1,width=10,textvariable=self.kdxentryvar)
        self.kdxentry.grid(row=1,column=1,padx=5,pady=3)

        kdylabel=tk.Label(righttopframe1,text='Kdy',background=righttopframe1color)
        kdylabel.grid(row=1,column=2,padx=5,pady=3)

        self.kdyentryvar=tk.StringVar()
        self.kdyentry=tk.Entry(righttopframe1,width=10,textvariable=self.kdyentryvar)
        self.kdyentry.grid(row=1,column=3,padx=5,pady=3)

        kdzlabel=tk.Label(righttopframe1,text='Kdz',background=righttopframe1color)
        kdzlabel.grid(row=1,column=4,padx=5,pady=3)

        self.kdzentryvar=tk.StringVar()
        self.kdzentry=tk.Entry(righttopframe1,width=10,textvariable=self.kdzentryvar)
        self.kdzentry.grid(row=1,column=5,padx=5,pady=3)


        kixlabel=tk.Label(righttopframe1,text='Kix',background=righttopframe1color)
        kixlabel.grid(row=2,column=0,padx=5,pady=3)

        self.kixentryvar=tk.StringVar()
        self.kixentry=tk.Entry(righttopframe1,width=10,textvariable=self.kixentryvar)
        self.kixentry.grid(row=2,column=1,padx=5,pady=3)

        kiylabel=tk.Label(righttopframe1,text='Kiy',background=righttopframe1color)
        kiylabel.grid(row=2,column=2,padx=5,pady=3)

        self.kiyentryvar=tk.StringVar()
        self.kiyentry=tk.Entry(righttopframe1,width=10,textvariable=self.kiyentryvar)
        self.kiyentry.grid(row=2,column=3,padx=5,pady=3)

        kizlabel=tk.Label(righttopframe1,text='Kiz',background=righttopframe1color)
        kizlabel.grid(row=2,column=4,padx=5,pady=3)

        self.kizentryvar=tk.StringVar()
        kizentry=tk.Entry(righttopframe1,width=10,textvariable=self.kizentryvar)
        kizentry.grid(row=2,column=5,padx=5,pady=3)

        tmzlabel=tk.Label(righttopframe1,text='tmz',background=righttopframe1color)
        tmzlabel.grid(row=3,column=4,padx=5,pady=5)

        self.tmzentryvar=tk.StringVar()
        tmzentry=tk.Entry(righttopframe1,width=10,textvariable=self.tmzentryvar)
        tmzentry.grid(row=3,column=5,padx=5,pady=5)

        #righttopframe2
        self.sendKvaluesbutton=tk.Button(righttopframe2,text='Send K values',background='white')
        self.sendKvaluesbutton.grid(row=0,column=0,padx=5,pady=5)

        self.readKvaluesbutton=tk.Button(righttopframe2,text='Read K values',background='white')
        self.readKvaluesbutton.grid(row=0,column=1,padx=5,pady=5)

        self.savebutton=tk.Button(righttopframe2,text='Save',background='white')
        self.savebutton.grid(row=0,column=2,padx=5,pady=5)

        #righttopframe3
        self.initTrajbutton=tk.Button(righttopframe3,text='Init',background='white')
        self.initTrajbutton.grid(row=0,column=0,padx=5,pady=5)

        self.startTrajbutton=tk.Button(righttopframe3,text='Start',background='white')
        self.startTrajbutton.grid(row=0,column=1,padx=5,pady=5)

        self.stopTrajbutton=tk.Button(righttopframe3,text='Stop',background='white')
        self.stopTrajbutton.grid(row=0,column=2,padx=5,pady=5)

        #Left
        lefttopcolor='light grey'
        lefttopframe=tk.Frame(leftframe,relief='raised',borderwidth=1,background=lefttopcolor)
        lefttopframe.pack(side=tk.TOP,fill=tk.BOTH,expand=False)

        leftbotcolor='light grey'
        leftbotframe=tk.Frame(leftframe,relief='raised',borderwidth=1,background=leftbotcolor)
        leftbotframe.pack(side=tk.TOP,fill=tk.BOTH,expand=True)

        #Lefttopframe
        leftlabel=tk.Label(lefttopframe,text='Axis Management',background=lefttopcolor,font=15)
        leftlabel.pack(side=tk.TOP)

        lefttopframe2=tk.Frame(lefttopframe,background=lefttopcolor)
        lefttopframe2.pack(side=tk.BOTTOM)

        self.clearxbuttoncolor='white'
        self.clearxbutton=tk.Button(lefttopframe2,text='Clear X',background=self.clearxbuttoncolor)
        self.clearxbutton.grid(row=0,column=0,padx=10,pady=5)

        self.clearybuttoncolor='white'
        self.clearybutton=tk.Button(lefttopframe2,text='Clear Y',background=self.clearybuttoncolor)
        self.clearybutton.grid(row=0,column=1,padx=10,pady=5)

        self.clearzbuttoncolor='white'
        self.clearzbutton=tk.Button(lefttopframe2,text='Clear Z',background=self.clearzbuttoncolor)
        self.clearzbutton.grid(row=0,column=2,padx=10,pady=5)

        self.clearFFbuttoncolor='white'
        self.clearFFbutton=tk.Button(lefttopframe2,text='Clear FF',background=self.clearFFbuttoncolor)
        self.clearFFbutton.grid(row=0,column=3,padx=10,pady=5)

        self.importxbuttoncolor='white'
        self.importxbutton=tk.Button(lefttopframe2,text='Import X',background=self.importxbuttoncolor)
        self.importxbutton.grid(row=1,column=0,padx=10,pady=5)

        self.importybuttoncolor='white'
        self.importybutton=tk.Button(lefttopframe2,text='Import Y',background=self.importybuttoncolor)
        self.importybutton.grid(row=1,column=1,padx=10,pady=5)

        self.importzbuttoncolor='white'
        self.importzbutton=tk.Button(lefttopframe2,text='Import Z',background=self.importzbuttoncolor)
        self.importzbutton.grid(row=1,column=2,padx=10,pady=5)

        self.importFFbuttoncolor='white'
        self.importFFbutton=tk.Button(lefttopframe2,text='Import FF',background=self.importFFbuttoncolor)
        self.importFFbutton.grid(row=1,column=3,padx=10,pady=5)

        self.clearimportbuttoncolor='white'
        self.clearimportbutton=tk.Button(lefttopframe2,text='Clear Import',background=self.clearimportbuttoncolor)
        self.clearimportbutton.grid(row=3,column=0,columnspan=2,padx=10,pady=5)

        self.downloadAxisbuttoncolor='white'
        self.downloadAxisbutton=tk.Button(lefttopframe2,text='Download Axis',background=self.downloadAxisbuttoncolor)
        self.downloadAxisbutton.grid(row=3,column=2,columnspan=2,padx=10,pady=5)

        #Leftbotframe
        leftbotlabel=tk.Label(leftbotframe,text='Data Acquisition',background=leftbotcolor,font=15)
        leftbotlabel.pack(side=tk.TOP)

        leftbotframe2=tk.Frame(leftbotframe,background=leftbotcolor)
        leftbotframe2.pack(side=tk.TOP)

        self.extractdatabuttoncolor='white'
        self.extractdatabutton=tk.Button(leftbotframe2,text='Extract Data',background=self.extractdatabuttoncolor)
        self.extractdatabutton.grid(row=0,column=0,padx=10,pady=5)

        self.cleardatabuttoncolor='white'
        self.cleardatabutton=tk.Button(leftbotframe2,text='Clear Data',background=self.cleardatabuttoncolor)
        self.cleardatabutton.grid(row=0,column=1)

        self.saverawdatabuttoncolor='white'
        self.saverawdatabutton=tk.Button(leftbotframe2,text='Save Raw Data',background=self.saverawdatabuttoncolor)
        self.saverawdatabutton.grid(row=1,column=0,columnspan=2)




def mainWindow():
    root = tk.Tk()
    root.geometry("1000x500+200+200")
    app = Application(root)
    return(app, root)
