#############################################################################################
# This code is property of the individual created:
# All rights to the code are reserved
# Unothorized use, disctrubution or any adaptation of the code will result in ligal actions
#############################################################################################


#region ----------------------- Imports -------------------------
import pandas as pd
from enum import Enum
import os
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
        print(self)

    def __repr__(self):
        return f"Device index: {self.index} located: {self.locationxy} and device passed the test {self.__passed}"
    
    def __call__(self, *args, **kwds):
        attrs=vars(self)
        return (", ".join("%s: %s" % item for item in attrs.items()))
    
    def Get_column_Names(self)->list:
        return self.df.columns
    
    def Get_average_of_column(self,columnindex):
        return self.df[self.df.columns[columnindex]].mean()
    

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
        filename=os.path.basename(datapath)
        try:
            _x=int(filename[0])
            _y=int(filename[2])
        except:
            _x="N/a"
            _y="N/a"
        return _x,_y
#endregion

#region ----------------------- AutoTest Class -----------------

class AutoTest:
    def __init__(self,FolderPath):
        self.Name=FolderPath
        self.ListOfTests=AutoTest.LoadTestData(FolderPath)
        self.NumberOfTests=len(self.ListOfTests)
        self.SuccessRate=AutoTest.Get_yield(self.ListOfTests)
        self.mergeddf=AutoTest.Get_Merge_DF(self)
        print(self)
        TestList.append(self)

    def __repr__(self):
        return f"Test has name: {self.Name} with number of test {self.NumberOfTests} and pesentage pass of {100*self.SuccessRate}"
    
    def Get_Merge_DF(self):
        ListofDF=[]
        for device in self.ListOfTests:
            ListofDF.append(device.df)
        merge=pd.concat(ListofDF)
        return merge

    def Get_average_of_all_columns(self):
        templist=[]
        for column in self.mergeddf.columns:
            templist.append(self.mergeddf[column].mean())
        return templist

    def LoadTestData(Folder)->list[Device]:
        templist=[]
        for i,name in enumerate(os.listdir(Folder)):
            templist.append(Device(f"{Folder}/{name}",i,True))
        return templist

    def Get_yield(ListofTests:list[Device])->float:
        """Returns a float number from 0 to 1
        with 1 all test were successfull and 0 none"""
        count=0
        for i,device in enumerate(ListofTests):
            if device.passed:
                count+=1
        return count/len(ListofTests)



# public data
TestList:list[Device]=[]



