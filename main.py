#########################################################################################
#                                                                                       #
#Software to control and extract data from the skating robot PRoPat.                    #
#                                                                                       #
#                                                                                       #
#Author: Gabriel Boucher                                                                #
#                                                                                       #
#########################################################################################

#Import modules needed
import serial as sr
import tkinter as tk
import re


#Class definition for the things to display and communicate
class controllerPIDdisplay():                              #PID controller to display only
    def __init__(self, kp=1, ki=0.001, kd=0.05):
        self.__kp = kp
        self.__ki = ki
        self.__kd = kd

    def changeKpValue(self,value):
        self.__kp = value

    def changeKiValue(self,value):
        self.__ki = value

    def changeKdValue(self,value):
        self.__kd = value

    def printKValues(self):
        print(self.__kp, self.__ki, self.__kd)

    def extractValues(self,stringToScan):
        extracted_stuff = re.findall(r"[-+]?\d*\.\d+|\d+",stringToScan)

class controllerPIDsend(controllerPIDdisplay):              #PID controller values to send

    def sendNewData(self):
        #Method to send stuff via serial
        a=1

class defAxis():                                            #Points to send through serial
    def __init__(self):
        self.__Points = [None]*768

    def addPoint(self,position,value):
        self.__Points[position] = value

    def clearPoints(self):
        for i in range(len(self.__Points)):
            self.__Points[i] = None

    def sendPTS(self):
        #Method to send stuff via serial
        a=1


class dataAcquisition():                                    #Here's the data recieved by the serial port from SD card
    def __init__(self):
        self.__data = [[None]*7]
        self.__position = 0

    def extractValues(self,stringToScan):
        extracted_stuff = re.findall(r"[-+]?\d*\.\d+|\d+",stringToScan)
        self.__data += extracted_stuff

    def clearData(self):
        slef.__data=[[None]*7]

##############################################Class definition for the application####################################################


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


        rightcolor='red'
        rightframe=tk.Frame(self,relief='raised',borderwidth=1,background=rightcolor)
        rightframe.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)

        leftcolor='grey'
        leftframe=tk.Frame(self,relief='raised',borderwidth=1,background=leftcolor)
        leftframe.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)



        #Buttons and texts for the application
        #Bottom
        comlabel=tk.Label(bottomframe,text='COM',background=bottomcolor)
        comlabel.pack(side=tk.LEFT,padx=5,pady=5)

        portentryvar=tk.StringVar()
        portentryvar.set("1")
        portentry=tk.Entry(bottomframe,width=7,textvariable=portentryvar)
        portentry.pack(side=tk.LEFT,padx=5,pady=5)


        okbutton=tk.Button(bottomframe,text='CONNECT')
        okbutton.pack(side=tk.LEFT)

        quitButton = tk.Button(bottomframe,text='DISCONNECT',command=self.quit)
        quitButton.pack(side=tk.LEFT, padx=5, pady=5)

        #Right
        Rightlabel=tk.Label(rightframe,text='PID Management',background=rightcolor,font=15)
        Rightlabel.pack(side=tk.TOP)

        righttopframe1color='blue'
        righttopframe1=tk.Frame(rightframe,background=righttopframe1color)
        righttopframe1.pack(side=tk.TOP)

        #Righttopframe1
        kpxlabel=tk.Label(righttopframe1,text='Kpx',background=righttopframe1color)
        kpxlabel.grid(row=0,column=0,padx=5,pady=3)

        kpxentryvar=tk.StringVar()
        kpxentry=tk.Entry(righttopframe1,width=10,textvariable=kpxentryvar)
        kpxentry.grid(row=0,column=1,padx=5,pady=3)

        kpylabel=tk.Label(righttopframe1,text='Kpy',background=righttopframe1color)
        kpylabel.grid(row=0,column=2,padx=5,pady=3)

        kpyentryvar=tk.StringVar()
        kpyentry=tk.Entry(righttopframe1,width=10,textvariable=kpyentryvar)
        kpyentry.grid(row=0,column=3,padx=5,pady=3)

        kpzlabel=tk.Label(righttopframe1,text='Kpz',background=righttopframe1color)
        kpzlabel.grid(row=0,column=4,padx=5,pady=3)

        kpzentryvar=tk.StringVar()
        kpzentry=tk.Entry(righttopframe1,width=10,textvariable=kpzentryvar)
        kpzentry.grid(row=0,column=5,padx=5,pady=3)


        kdxlabel=tk.Label(righttopframe1,text='Kdx',background=righttopframe1color)
        kdxlabel.grid(row=1,column=0,padx=5,pady=3)

        kdxentryvar=tk.StringVar()
        kdxentry=tk.Entry(righttopframe1,width=10,textvariable=kpxentryvar)
        kdxentry.grid(row=1,column=1,padx=5,pady=3)

        kdylabel=tk.Label(righttopframe1,text='Kdy',background=righttopframe1color)
        kdylabel.grid(row=1,column=2,padx=5,pady=3)

        kdyentryvar=tk.StringVar()
        kdyentry=tk.Entry(righttopframe1,width=10,textvariable=kpyentryvar)
        kdyentry.grid(row=1,column=3,padx=5,pady=3)

        kdzlabel=tk.Label(righttopframe1,text='Kdz',background=righttopframe1color)
        kdzlabel.grid(row=1,column=4,padx=5,pady=3)

        kdzentryvar=tk.StringVar()
        kdzentry=tk.Entry(righttopframe1,width=10,textvariable=kpzentryvar)
        kdzentry.grid(row=1,column=5,padx=5,pady=3)


        kixlabel=tk.Label(righttopframe1,text='Kix',background=righttopframe1color)
        kixlabel.grid(row=2,column=0,padx=5,pady=3)

        kixentryvar=tk.StringVar()
        kixentry=tk.Entry(righttopframe1,width=10,textvariable=kpxentryvar)
        kixentry.grid(row=2,column=1,padx=5,pady=3)

        kiylabel=tk.Label(righttopframe1,text='Kiy',background=righttopframe1color)
        kiylabel.grid(row=2,column=2,padx=5,pady=3)

        kiyentryvar=tk.StringVar()
        kiyentry=tk.Entry(righttopframe1,width=10,textvariable=kpyentryvar)
        kiyentry.grid(row=2,column=3,padx=5,pady=3)

        kizlabel=tk.Label(righttopframe1,text='Kiz',background=righttopframe1color)
        kizlabel.grid(row=2,column=4,padx=5,pady=3)

        kizentryvar=tk.StringVar()
        kizentry=tk.Entry(righttopframe1,width=10,textvariable=kpzentryvar)
        kizentry.grid(row=2,column=5,padx=5,pady=3)


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

        importxbuttoncolor='white'
        importxbutton=tk.Button(lefttopframe2,text='Import X',background=importxbuttoncolor)
        importxbutton.grid(row=1,column=0,padx=10,pady=5)

        importybuttoncolor='white'
        importybutton=tk.Button(lefttopframe2,text='Import X',background=importybuttoncolor)
        importybutton.grid(row=1,column=1,padx=10,pady=5)

        importzbuttoncolor='white'
        importzbutton=tk.Button(lefttopframe2,text='Import X',background=importzbuttoncolor)
        importzbutton.grid(row=1,column=2,padx=10,pady=5)

        importFFbuttoncolor='white'
        importFFbutton=tk.Button(lefttopframe2,text='Import X',background=importFFbuttoncolor)
        importFFbutton.grid(row=1,column=3,padx=10,pady=5)

        clearimportbuttoncolor='white'
        clearimportbutton=tk.Button(lefttopframe2,text='Clear Import',background=clearimportbuttoncolor)
        clearimportbutton.grid(row=3,column=0,columnspan=2,padx=10,pady=5)

        downloadAxisbuttoncolor='white'
        downloadAxisbutton=tk.Button(lefttopframe2,text='Download Axis',background=downloadAxisbuttoncolor)
        downloadAxisbutton.grid(row=3,column=2,columnspan=2,padx=10,pady=5)

        #Leftbotframe
        leftbotlabel=tk.Label(leftbotframe,text='Data Acquisition',background=leftbotcolor,font=15)
        leftbotlabel.pack(side=tk.TOP)







def mainWindow():
    root = tk.Tk()
    root.geometry("1000x500+200+200")
    app = Application(root)
    root.mainloop()



#Main program
mainWindow()
