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

#Class definition for the application


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

        leftcolor='gold'
        leftframe=tk.Frame(self,relief='raised',borderwidth=1,background=leftcolor)
        leftframe.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

        lefttopcolor='green'
        lefttopframe=tk.Frame(leftframe,relief='raised',borderwidth=1,background=lefttopcolor)
        lefttopframe.pack(side=tk.TOP,fill=tk.BOTH,expand=False)

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
        Rightlabel=tk.Label(rightframe,text='PID Management',background=rightcolor)
        Rightlabel.pack(side=tk.TOP)

        #Lefttop
        leftlabel=tk.Label(lefttopframe,text='Axis Management',background=lefttopcolor)
        leftlabel.pack(side=tk.TOP)






def mainWindow():
    root = tk.Tk()
    root.geometry("1000x500+200+200")
    app = Application(root)
    root.mainloop()



#Main program
mainWindow()
