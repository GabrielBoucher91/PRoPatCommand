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
import tkinter as tk
import re



#Class definition for backhand of the PRoPat Command software

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

    def sendNewData(self,Application):
        #Method to send stuff via serial
        Application.kdzentryvar.set('456')                  #TEST WORKS!!!!
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

