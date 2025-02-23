#############################################################################################
# This code is property of the individual created:
# All rights to the code are reserved
# Unothorized use, disctrubution or any adaptation of the code will result in ligal actions
#############################################################################################

#region ----------------------- Imports -------------------------

import Dependencies.DataHandler as DH
import Dependencies.UIModule as UI
import Dependencies.PlottingData as PTD
#endregion

def UT_CreateOBJ(file):
    test=DH.Device(file,0,True)
    DH.DeviceList.append(test)
    print(DH.DeviceList)
    PTD.PlotXY(DH.DeviceList[0].df)


UT_CreateOBJ("Data.csv")

