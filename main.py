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

#Class definition for the things to display and communicate

class controllerPID():
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

class defAxis():
    def __init__(self):
        self.__Points = [None]*768
    def addPoint(self,position,value):
        self.__Points[position] = value
    def clearPoints(self):
        for i in range(len(self.__Points)):
            self.__Points[i] = None




#Class definition for the application
class Application(tk.Frame):
    def __init(self,parent):
        tk.Frame.__init__(self, parent, background="white")
        self.parent=parent
        self.initUI()
    def initUI(self):
        self.parent.title("PRoPat Command Software")
        self.pack(fill=tk.BOTH,expand=1)

def mainWindow():
    root=tk.Tk()
    root.geometry("500x300+300+300")
    app=Application(root)
    root.mainloop()




mainWindow()
