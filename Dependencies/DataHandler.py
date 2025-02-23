#############################################################################################
# This code is property of the individual created:
# All rights to the code are reserved
# Unothorized use, disctrubution or any adaptation of the code will result in ligal actions
#############################################################################################


#region ----------------------- Imports -------------------------
import pandas as pd
import os
import json
import gc
from enum import Enum
from dataclasses import dataclass,fields
#endregion

#region ----------------------- Device Class --------------------
class Device:
    """ Device Class
    Generates a Device obj
    NOTE: This code requires higher level of authoraty to change"""
    def __init__(self,Filepath:str,index:int,passed:bool,**kwargs):
        self.df=Device.Get_data(Filepath)
        self.index=index
        self.__passed=passed
        self.locationxy=Device.Get_x_y(Filepath)
        print(self())


    def __repr__(self):
        return f"Device index: {self.index} located: {self.locationxy} and device passed the test {self.__passed}"
    
    def __call__(self, *args, **kwds):
        attrs=vars(self)
        return (", ".join("%s: %s" % item for item in attrs.items()))
    
    @property
    def passed(self):
        return self.__passed
    
    @passed.setter              # Setter the property only admin can change to true
    def passed(self,value:tuple):
        try:
            newSeter,AdminBool=value
            if newSeter and AdminBool:
                self.__passed=True
            else:
                self.__passed=False
        except ValueError:
            print("Error: Expected a tuple with two values (newSeter, AdminBool).")
            self.__passed = False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            self.__passed = False
            
    def Get_data(datapath):
        try:
            df=pd.read_csv(datapath,encoding='utf-8')
        except Exception as e:
            print(f"Data not in the correct format: {e}")
            return
        return df

    def Get_x_y(datapath):
        try:
            _x=int(datapath[0:3])
            _y=int(datapath[4:7])
        except:
            _x="N/a"
            _y="N/a"
        return _x,_y
#endregion

# public data
DeviceList:list[Device]=[]


