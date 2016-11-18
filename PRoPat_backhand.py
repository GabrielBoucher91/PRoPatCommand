#########################################################################################
#                                                                                       #
#Backhand part of the software										                    #
#                                                                                       #
#                                                                                       #
#Author: Gabriel Boucher                                                                #
#                                                                                       #
#########################################################################################





#Import modules needed
import serial as sr
import re



#Class definition for backhand of the PRoPat Command software

class controllerPID():                              #PID controller to display only
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

    def copyPIDValues(self,other,Application,Axis):
    	self.__kp=other.__kp
    	self.__ki=other.__ki
    	self.__kd=other.__kd
    	self.updateKvalues(Application,Axis)

    def updateKvalues(self,Application,Axis):
    	if(Axis=='X'):
    		Application.kpxentryvar.set(str(self.__kp))
    		Application.kixentryvar.set(str(self.__ki))
    		Application.kdxentryvar.set(str(self.__kd))
    	elif(Axis=='Y'):
    		Application.kpyentryvar.set(str(self.__kp))
    		Application.kiyentryvar.set(str(self.__ki))
    		Application.kdyentryvar.set(str(self.__kd))
    	elif(Axis=='Z'):
    		Application.kpzentryvar.set(str(self.__kp))
    		Application.kizentryvar.set(str(self.__ki))
    		Application.kdzentryvar.set(str(self.__kd))





    

class defAxis():                                            #Points to send through serial
    def __init__(self):
        self.__Points = [None]*768

    def addPoint(self,position,value):
        self.__Points[position] = value

    def clearPoints(self):
        for i in range(len(self.__Points)):
            self.__Points[i] = None

    def sendPTS(self):
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

