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
import matplotlib.pyplot as plt
import time



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
        self.__data = []
        self.__X1 = []
        self.__X2 = []
        self.__Y1 = []
        self.__Y2 = []
        self.__Z1 = []
        self.__Z2 = []
        self.__FF = []

    def convertValues(self,stringToScan):
        extracted_stuff = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+",stringToScan)
        extracted_stuff = [float(i) for i in extracted_stuff]
        self.__data += [extracted_stuff]

    def clearData(self, other, cport):
        self.__data = []
        self.__X1 = []
        self.__X2 = []
        self.__Y1 = []
        self.__Y2 = []
        self.__Z1 = []
        self.__Z2 = []
        self.__FF = []
        other.data = []
        cport.write(b'C\r\n')

    def printData(self):
        print(self.__data)

    def dispatchData(self):
        for i in self.__data:
            self.__X1 += [i[0]]
            self.__X2 += [i[1]]
            self.__Y1 += [i[2]]
            self.__Y2 += [i[3]]
            self.__Z1 += [i[4]]
            self.__Z2 += [i[5]]
            self.__FF += [i[6]]

    def displayGraph(self):
        plt.figure(1)
        plt.plot(self.__X1, label="Encoder")
        plt.plot(self.__X2, label="Command")
        plt.title("X axis position and command")
        plt.legend()
        plt.ylabel("Encoder position")
        plt.figure(2)
        plt.plot(self.__Y1, label="Encoder")
        plt.plot(self.__Y2, label="Command")
        plt.title("Y axis position and command")
        plt.legend()
        plt.ylabel("Encoder position")
        plt.figure(3)
        plt.plot(self.__Z1, label="Encoder")
        plt.plot(self.__Z2, label="Command")
        plt.title("Z axis position and command")
        plt.legend()
        plt.ylabel("Encoder position")
        plt.figure(4)
        plt.plot(self.__FF, label="Feed Forward")
        plt.title("Feed Forward value")
        plt.legend()
        plt.ylabel("PWM value")
        plt.figure(5)
        Err_x = [i - j for i, j in zip(self.__X2, self.__X1)]
        plt.plot(Err_x, label="Error")
        plt.title("Error for the X axis")
        plt.legend()
        plt.ylabel("Encoder count")
        plt.figure(6)
        Err_y = [i - j for i, j in zip(self.__Y2, self.__Y1)]
        plt.plot(Err_y, label="Error")
        plt.title("Error for the Y axis")
        plt.legend()
        plt.ylabel("Encoder count")
        plt.figure(7)
        Err_z = [i - j for i, j in zip(self.__Z2, self.__Z1)]
        plt.plot(Err_z, label="Error")
        plt.title("Error for the Z axis")
        plt.legend()
        plt.ylabel("Encoder count")

        plt.show()


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
    file=fd.askopenfile(parent=root,filetypes=[("Text files", "*.txt")])
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
        Application.importFFbuttoncolor='green'
    
def clearAxis(Application, cport, Axname):
    if(Axname == 'X'):
        cport.write(b"pem333\r\n")
        Application.clearxbutton.configure(background='green')
        Application.clearxbuttoncolor = 'green'
    if(Axname == 'Y'):
        cport.write(b"pem666\r\n")
        Application.clearybutton.configure(background='green')
        Application.clearybuttoncolor = 'green'
    if(Axname == 'Z'):
        cport.write(b"pem999\r\n")
        Application.clearzbutton.configure(background='green')
        Application.clearzbuttoncolor = 'green'
    if(Axname == 'FF'):
        cport.write(b"pem666\r\n")
        Application.clearFFbutton.configure(background='green')
        Application.clearFFbuttoncolor = 'green'


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


def downloadAxis(Application,cport,X,Y,Z,FF):
    if Application.importxbuttoncolor == 'green':
        if Application.clearxbuttoncolor != 'green':
            cport.write(b"pem333\r\n")
            time.sleep(0.5)

        for i in range(768):
            stringtosend = 'pam'+str(i)+'dm'+str(X.getPoint(i))+'\r\n'
            cport.write(bytes(stringtosend, encoding='utf-8'))
            print(stringtosend)
            time.sleep(0.09)
        Application.clearxbutton.configure(background='white')
        Application.clearxbuttoncolor = 'white'
        Application.importxbutton.configure(background='white')
        Application.importxbuttoncolor = 'white'
        X.clearPoints()

    if Application.importybuttoncolor == 'green':
        if Application.clearybuttoncolor != 'green':
            cport.write(b"pem666\r\n")
            time.sleep(0.5)

        for i in range(768):
            stringtosend = 'pam'+str(i+768)+'dm'+str(Y.getPoint(i))+'\r\n'
            cport.write(bytes(stringtosend, encoding='utf-8'))
            time.sleep(0.09)
        Application.clearybutton.configure(background='white')
        Application.clearybuttoncolor = 'white'
        Application.importybutton.configure(background='white')
        Application.importybuttoncolor = 'white'
        Y.clearPoints

    if Application.importzbuttoncolor == 'green':
        if Application.clearzbuttoncolor != 'green':
            cport.write(b"pem666\r\n")
            time.sleep(0.5)

        for i in range(768):
            stringtosend = 'pam'+str(i+1536)+'dm'+str(Z.getPoint(i))+'\r\n'
            cport.write(bytes(stringtosend, encoding='utf-8'))
            time.sleep(0.09)
        Application.clearzbutton.configure(background='white')
        Application.clearzbuttoncolor = 'white'
        Application.importzbutton.configure(background='white')
        Application.importzbuttoncolor = 'white'
        Z.clearPoints()

    if Application.importFFbuttoncolor == 'green':
        if Application.clearFFbuttoncolor != 'green':
            cport.write(b"pem333\r\n")
            time.sleep(0.5)

        for i in range(768):
            stringtosend = 'pam'+str(i+2304)+'dm'+str(FF.getPoint(i))+'\r\n'
            cport.write(bytes(stringtosend, encoding='utf-8'))
            time.sleep(0.03)
        Application.clearFFbutton.configure(background='white')
        Application.clearFFbuttoncolor = 'white'
        Application.importFFbutton.configure(background='white')
        Application.importFFbuttoncolor = 'white'
        FF.clearPoints()

def savePIDvalues(cport):
    cport.write(b'Save\r\n')


def extractData(dataAq, daqraw, cport):
    cport.flushInput()
    cport.flushOutput()
    cport.write(b'T\r\n')
    retvalue = []
    block = int(str(cport.readline().decode("utf-8")))
    print(block)
    row = 1
    retvalue = cport.readlines()
    for i in retvalue:
        daqraw.data += [str(i.decode("utf-8"))]
    retvalue = []
    for i in daqraw.data:
        dataAq.convertValues(i)
    dataAq.dispatchData()
    dataAq.displayGraph()

def saveRawData(daqraw):
    file = fd.asksaveasfile(mode="w", defaultextension="*.txt", filetypes=[("Text files", "*.txt")])
    for i in daqraw.data:
        file.write(i)
    file.close()

def initTraj(cport):
    cport.write(b'pcm414\r\n')

def startTraj(cport):
    cport.write(b'pcm424\r\n')

def stopTraj(cport):
    cport.write(b'pcm404\r\n')

def extractNumbers(a):
    return re.findall(r"[-+]?\d*\.*\d+", a)

