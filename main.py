#########################################################################################
#                                                                                       #
#Software to control and extract data from the skating robot PRoPat.                    #
#                                                                                       #
#                                                                                       #
#Author: Gabriel Boucher                                                                #
#                                                                                       #
#########################################################################################

#Import modules needed

import PRoPat_backhand as PPb
import PRoPat_fronthand as PPf



###########################TEST############################
contZ=PPb.controllerPIDsend()
###########################################################



##############################################Class definition for the application####################################################





def buildMain(froot,fapp):
    fapp.okbutton.config(command=lambda: contZ.sendNewData(fapp))
    froot.mainloop()




#Main program

app_root=PPf.mainWindow()

buildMain(app_root[1],app_root[0])

