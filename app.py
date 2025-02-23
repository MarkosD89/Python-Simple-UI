#############################################################################################
# This code is property of the individual created:
# All rights to the code are reserved
# Unothorized use, disctrubution or any adaptation of the code will result in ligal actions
#############################################################################################

#region ----------------------- Imports -------------------------

import tkinter as tk
from tkinter import ttk
import Dependencies.DataHandler as DH
import Dependencies.UIModule as UI
#endregion

class MyApp:
    def __init__(self, root:tk.Tk):
        self.root = root
        self.root.title("My app")
        self.root.geometry("400x500")
        self.MainMenu=tk.Menu(root)
        self.root.config(menu=self.MainMenu)

        self.FileMenu=tk.Menu(self.MainMenu,tearoff="off")
        #...
        self.MainMenu.add_cascade(label="File",menu=self.FileMenu)
        #...
        self.FileMenu.add_command(label="Load .csv Data",command=lambda:UI.Get_data(root))

        self.PlotMenu=tk.Menu(self.MainMenu,tearoff="off")
        #...
        self.MainMenu.add_cascade(label="Plots",menu=self.PlotMenu)
        #...
        self.PlotMenu.add_command(label="Plot_data",command=lambda:UI.Plot_data(root))

def main():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()