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
    #Bottom
    fapp.okbutton.config(command=lambda: PPb.openPort(fapp))


    #Left
    fapp.clearimportbutton.config(command=lambda: PPb.clearimport(fapp,froot,Xaxis,Yaxis,Zaxis,FFaxis))
    fapp.importxbutton.config(command=lambda: PPb.getfile(fapp,froot,Xaxis,'X'))
    fapp.importybutton.config(command=lambda: PPb.getfile(fapp,froot,Yaxis,'Y'))
    fapp.importzbutton.config(command=lambda: PPb.getfile(fapp,froot,Zaxis,'Z'))
    fapp.importFFbutton.config(command=lambda: PPb.getfile(fapp,froot,FFaxis,'FF'))

    #Right
    fapp.readKvaluesbutton.config(command=lambda: PPb.getPIDValues(fapp,contX,contY,contZ))
    fapp.sendKvaluesbutton.config(command=lambda: PPb.sendPIDValues(fapp,contX,contY,contZ))


    froot.mainloop()




#Main program

app_root=PPf.mainWindow()

buildMain(app_root[1],app_root[0])

