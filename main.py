#########################################################################################
#                                                                                       #
#Software to control and extract data from the skating robot PRoPat.                    #
#                                                                                       #
#                                                                                       #
#Author: Gabriel Boucher                                                                #
#                                                                                       #
#########################################################################################

#Import modules needed

import PRoPat_backend as PPb
import PRoPat_frontend as PPf
import serial as sr


###########################TEST############################

###########################################################



##############################################Class definition for the application####################################################





def buildMain(froot,fapp):
    #Creating objects in the backend of the application
    contY=PPb.controllerPID()
    contZ=PPb.controllerPID()
    contX=PPb.controllerPID()

    Xaxis=PPb.defAxis()
    Yaxis=PPb.defAxis()
    Zaxis=PPb.defAxis()
    FFaxis=PPb.defAxis()

    daq=PPb.dataAcquisitionRaw()

    datAq = PPb.dataAcquisition()

    cport=sr.Serial()


    #Assignation of the methods for each buttons
    #Bottom
    fapp.okbutton.config(command=lambda: PPb.openPort(fapp, cport, contX, contY, contZ))
    fapp.quitButton.config(command=lambda: PPb.disconnect(fapp, cport))


    #Left

    fapp.clearxbutton.config(command=lambda: PPb.clearAxis(fapp,cport,'X'))
    fapp.clearybutton.config(command=lambda: PPb.clearAxis(fapp,cport,'Y'))
    fapp.clearzbutton.config(command=lambda: PPb.clearAxis(fapp,cport,'Z'))
    fapp.clearFFbutton.config(command=lambda: PPb.clearAxis(fapp,cport,'FF'))

    fapp.clearimportbutton.config(command=lambda: PPb.clearimport(fapp,froot,Xaxis,Yaxis,Zaxis,FFaxis))
    fapp.importxbutton.config(command=lambda: PPb.getfile(fapp,froot,Xaxis,'X'))
    fapp.importybutton.config(command=lambda: PPb.getfile(fapp,froot,Yaxis,'Y'))
    fapp.importzbutton.config(command=lambda: PPb.getfile(fapp,froot,Zaxis,'Z'))
    fapp.importFFbutton.config(command=lambda: PPb.getfile(fapp,froot,FFaxis,'FF'))

    fapp.downloadAxisbutton.config(command=lambda: PPb.downloadAxis(fapp, cport, Xaxis, Yaxis, Zaxis, FFaxis))

    fapp.extractdatabutton.config(command=lambda: PPb.extractData(datAq, daq, cport))
    fapp.cleardatabutton.config(command=lambda: datAq.clearData(daq, cport))
    fapp.saverawdatabutton.config(command=lambda: PPb.saveRawData(daq))

    #Right
    fapp.readKvaluesbutton.config(command=lambda: PPb.getPIDValues(fapp,contX,contY,contZ,cport))
    fapp.sendKvaluesbutton.config(command=lambda: PPb.sendPIDValues(fapp,contX,contY,contZ,cport))
    fapp.sendMaxTorquebutton.config(command=lambda: PPb.sendMaxTorque(fapp,cport))
    fapp.savebutton.config(command=lambda: PPb.savePIDvalues(cport))

    fapp.initTrajbutton.config(command=lambda: PPb.initTraj(cport))
    fapp.startTrajbutton.config(command=lambda: PPb.startTraj(cport))
    fapp.stopTrajbutton.config(command=lambda: PPb.stopTraj(cport))




    froot.mainloop()




#Main program

app_root=PPf.mainWindow()

buildMain(app_root[1],app_root[0])

