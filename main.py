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


    #Assignation of the methods for each buttons
    fapp.okbutton.config(command=lambda: PPb.openPort(fapp))

    fapp.clearimportbutton.config(command=lambda: contZ.copyPIDValues(contX,fapp,'Z'))
    fapp.readKvaluesbutton.config(command=lambda: PPb.getPIDValues(fapp,contX,contY,contZ))
    fapp.sendKvaluesbutton.config(command=lambda: PPb.sendPIDValues(fapp,contX,contY,contZ))
    fapp.importxbutton.config(command=lambda: PPb.getfile(Xaxis,froot))

    froot.mainloop()




#Main program

app_root=PPf.mainWindow()

buildMain(app_root[1],app_root[0])

