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
    contZ=PPb.controllerPID()
    contX=PPb.controllerPID(2,3,4)

    fapp.okbutton.config(command=lambda: contZ.updateKvalues(fapp,'Z'))
    fapp.clearimportbutton.config(command=lambda: contZ.copyPIDValues(contX,fapp,'Z'))
    froot.mainloop()




#Main program

app_root=PPf.mainWindow()

buildMain(app_root[1],app_root[0])

