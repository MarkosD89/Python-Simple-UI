#############################################################################################
# This code is property of the individual created:
# All rights to the code are reserved
# Unothorized use, disctrubution or any adaptation of the code will result in ligal actions
#############################################################################################


#region ----------------------- Imports -------------------------
import tkinter as tk
import tkinter.filedialog as fdialog
import tkinter.messagebox as tkmessage
import tkinter.ttk as ttk
import time
import Dependencies.DataHandler as DH
import Dependencies.PlottingData as PTD
#endregion

class ProcessingWindow:
    def __init__(self,processName,TotalRepeats,MainRoot):
        self.start=time.time()
        self.NewWindow=tk.Toplevel(processName)
        self._currentProcess=0
        self.TotalRepeats=TotalRepeats
        self.BarLenght=200
        self._progressBar=ttk.Progressbar(self.NewWindow,orient=tk.HORIZONTAL,mode="determinate",length=self.BarLenght)
        self.NewWindowLable=tk.Label(self.NewWindow,text=f"Process: {self._currentProcess} out of {self.TotalRepeats}")
        self.NewWindowLable.grid(row=0,column=0)
        self._progressBar.grid(row=1,column=0)
        MainRoot.update()

    def BarUpdate(self,progress,MainRoot):
        self.end=time.time()
        self.etf=((self.end-self.start)*self.TotalRepeats)/(self._currentProcess+1)
        self._currentProcess=progress
        self._progressBar["value"]=100*(self._currentProcess/self.TotalRepeats)
        self.NewWindowLable["text"]=f"Process: {self._currentProcess} out of {self.TotalRepeats}"
        MainRoot.update()
        if self._currentProcess+1==self.TotalRepeats:
            self.NewWindow.destroy()

class Widgets:
    def New_label(Root,text,row,column,ColumnSpan):
        label = tk.Label(Root, text=text)
        label.grid(row=row,column=column, columnspan=ColumnSpan)
        return label

    def New_Button (Root,text,row,column,ColumnSpan):
        button = tk.Button(Root, text=text)
        button.grid(row=row,column=column, columnspan=ColumnSpan)
        return button

class SeconderyWindow:
    """Generate New windows with specific uses"""
    def __init__(self):
        #...
        pass
    #TODO add more Functionality
    #BUG found a bug in line ... fix...



def Build_new_note_book (MainRoot,Notelist,Autotest:DH.AutoTest):
    frame1 = ttk.Frame(Notelist)
    Notelist.add(frame1, text=Autotest)

    treeview1 = ttk.Treeview(frame1, columns=Autotest.ListOfTests[0].Get_column_Names())
    for i,name in enumerate(Autotest.ListOfTests[0].Get_column_Names()):
        treeview1.heading(f"#{i}", text=name)
    treeview1.insert("","end",values=Autotest.Get_average_of_all_columns())
    treeview1.grid(row=2,column=1)
    



def Get_data(MainRoot:tk):

    file = fdialog.askopenfilename(initialdir="Desktop", title="Select File", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    if file:
        device = DH.Device(file, 0, True)
        DH.TestList.append(device)  # Add the device to the list
    else:
        print("No file selected")

def Get_Folder(MainRoot:tk,Notelist:ttk.Notebook):
    folder=fdialog.askdirectory(initialdir="Desktop",title="Select Folder to load")
    if folder:
        DH.AutoTest(folder)
        Build_new_note_book(MainRoot,Notelist,DH.TestList[-1])

def Plot_data(MainRoot:tk):
    for data in DH.TestList:
        PTD.PlotXY(data.df)
