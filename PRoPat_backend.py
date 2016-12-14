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
import tkinter.filedialog as fd
import matplotlib.pyplot as pt



#Class definition for backend of the PRoPat Command software


class controllerPID():                              #PID controller to display only
    def __init__(self, kp=1, ki=0.001, kd=0.05):
        self.__kp = kp
        self.__ki = ki
        self.__kd = kd

    def getKpvalue(self):
        return(self.__kp)

    def getKivalue(self):
        return(self.__ki)

    def getKdvalue(self):
        return(self.__kd)

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





    

class defAxis():
    #Points to send through serial
    def __init__(self):
        self.__Points = [None]*768

    def addPoint(self,position,value):
        self.__Points[position] = value

    def clearPoints(self):
        for i in range(len(self.__Points)):
            self.__Points[i] = None

    def getPoint(self,position):
        return self.__Points[position]


class dataAcquisition():                                    #Here's the data recieved by the serial port from SD card
    def __init__(self):
        self.__data = [[None]*7]
        self.__position = 0

    def extractValues(self,stringToScan):
        extracted_stuff = re.findall(r"[-+]?\d*\.\d+|\d+",stringToScan)
        extracted_stuff = [int(i) for i in extracted_stuff]
        self.__data += [extracted_stuff]

    def clearData(self):
        self.__data=[[None]*7]

class dataAcquisitionRaw():
    def __init__(self):
        self.data = []



################################Methods for buttons######################################
def openPort(Application,cport,X,Y,Z):
    comport='COM'+Application.portentryvar.get()
    print(comport)
    cport.port=comport
    cport.baudrate=115200
    cport.timeout=1
    cport.open()
    print(cport.is_open)
    getPIDValues(Application,X,Y,Z,cport)

def disconnect(Application,cport):
    cport.close()

def getPIDValues(Application,X1,Y1,Z1,cport):
    print('Poulet 1')
    cport.write(b'r\r\n')
    print('Poulet 2')
    A=extractNumbers(str(cport.readline().decode("utf-8")))
    print('Poulet 3')
    Application.kpxentryvar.set(A[1])
    Application.kdxentryvar.set(A[2])
    Application.kixentryvar.set(A[3])
    Application.kpyentryvar.set(A[4])
    Application.kdyentryvar.set(A[5])
    Application.kiyentryvar.set(A[6])
    Application.kpzentryvar.set(A[7])
    Application.kdzentryvar.set(A[8])
    Application.kizentryvar.set(A[9])
    X1.changeKpValue(float(A[1]))
    X1.changeKdValue(float(A[2]))
    X1.changeKiValue(float(A[3]))
    Y1.changeKpValue(float(A[4]))
    Y1.changeKdValue(float(A[5]))
    Y1.changeKiValue(float(A[6]))
    Z1.changeKpValue(float(A[7]))
    Z1.changeKdValue(float(A[8]))
    Z1.changeKiValue(float(A[9]))
    print("New values arrived")




def sendPIDValues(Application,X2,Y2,Z2,cport):
    #Compares the values of the PID since last send/recieve and send the new values through serial port
    if float(Application.kpxentryvar.get())!=X2.getKpvalue():
        print(float(Application.kpxentryvar.get()))
        stringToSend="kpx"+str(Application.kpxentryvar.get()+"\r\n")
        cport.write(bytes(stringToSend, encoding='utf-8'))
        X2.changeKpValue(float(Application.kpxentryvar.get()))
    if float(Application.kixentryvar.get())!=X2.getKivalue():
        print(float(Application.kixentryvar.get()))
        stringToSend="kix"+str(Application.kixentryvar.get()+"\r\n")
        cport.write(bytes(stringToSend, encoding='utf-8'))
        X2.changeKiValue(float(Application.kixentryvar.get()))
    if float(Application.kdxentryvar.get())!=X2.getKdvalue():
        print(float(Application.kdxentryvar.get()))
        stringToSend="kdx"+str(Application.kdxentryvar.get()+"\r\n")
        cport.write(bytes(stringToSend, encoding='utf-8'))
        X2.changeKdValue(float(Application.kdxentryvar.get()))
    if float(Application.kpyentryvar.get())!=Y2.getKpvalue():
        print(float(Application.kpyentryvar.get()))
        stringToSend="kpy"+str(Application.kpyentryvar.get()+"\r\n")
        cport.write(bytes(stringToSend, encoding='utf-8'))
        Y2.changeKpValue(float(Application.kpyentryvar.get()))
    if float(Application.kiyentryvar.get())!=Y2.getKivalue():
        print(float(Application.kiyentryvar.get()))
        stringToSend="kiy"+str(Application.kiyentryvar.get()+"\r\n")
        cport.write(bytes(stringToSend, encoding='utf-8'))
        Y2.changeKiValue(float(Application.kiyentryvar.get()))
    if float(Application.kdyentryvar.get())!=Y2.getKdvalue():
        print(float(Application.kdyentryvar.get()))
        stringToSend="kdy"+str(Application.kdyentryvar.get()+"\r\n")
        cport.write(bytes(stringToSend, encoding='utf-8'))
        Y2.changeKdValue(float(Application.kdyentryvar.get()))
    if float(Application.kpzentryvar.get())!=Z2.getKpvalue():
        print(float(Application.kpzentryvar.get()))
        stringToSend="kpz"+str(Application.kpzentryvar.get()+"\r\n")
        cport.write(bytes(stringToSend, encoding='utf-8'))
        Z2.changeKpValue(float(Application.kpzentryvar.get()))
    if float(Application.kizentryvar.get())!=Z2.getKivalue():
        print(float(Application.kizentryvar.get()))
        stringToSend="kiz"+str(Application.kizentryvar.get()+"\r\n")
        cport.write(bytes(stringToSend, encoding='utf-8'))
        Z2.changeKiValue(float(Application.kizentryvar.get()))
    if float(Application.kdzentryvar.get())!=Z2.getKdvalue():
        print(float(Application.kdzentryvar.get()))
        stringToSend="kdz"+str(Application.kdzentryvar.get()+"\r\n")
        cport.write(bytes(stringToSend, encoding='utf-8'))
        Z2.changeKdValue(float(Application.kdzentryvar.get()))
    print("Finished sending new values")
    #Need send "Save\r\n" to make sure the data is saved in the flash memory


def getfile(Application,root,Ax,AxName):
    file=fd.askopenfile(parent=root,filetypes=[("Text files","*.txt")])
    i=0
    for lines in file:
        Ax.addPoint(i,int(lines))
        i+=1
    file.close()
    if(AxName=='X'):
        Application.importxbutton.configure(background='green')
        Application.importxbuttoncolor='green'
    if(AxName=='Y'):
        Application.importybutton.configure(background='green')
        Application.importybuttoncolor='green'
    if(AxName=='Z'):
        Application.importzbutton.configure(background='green')
        Application.importzbuttoncolor='green'
    if(AxName=='FF'):
        Application.importFFbutton.configure(background='green')
        Application.importxFFbuttoncolor='green'
    

def clearimport(Application,root,X,Y,Z,FF):
    X.clearPoints()
    Y.clearPoints()
    Z.clearPoints()
    FF.clearPoints()
    Application.importxbutton.configure(background='white')
    Application.importxbuttoncolor='white'
    Application.importybutton.configure(background='white')
    Application.importybuttoncolor='white'
    Application.importzbutton.configure(background='white')
    Application.importzbuttoncolor='white'
    Application.importFFbutton.configure(background='white')
    Application.importFFbuttoncolor='white'

def downloadAxis(Application,cport):
    cport.write(b'B\r\n')
    print(int(str(cport.readline().decode("utf-8"))))

def extractData(daq, cport):
    cport.write(b'T\r\n')
    retvalue = []
    block = int(str(cport.readline().decode("utf-8")))
    print(block)

    row = 1

    while(row <= block*17):
        retvalue += [str(cport.readline().decode("utf-8"))]
        row += 1

    daq.data += retvalue
    print(daq.data)
    print(len(daq.data))
    print([float(i) for i in extractNumbers(daq.data[0])])

def extractNumbers(a):
    return re.findall(r"[-+]?\d*\.*\d+", a)

