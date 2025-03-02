#############################################################################################
# This code is property of the individual created:
# All rights to the code are reserved
# Unothorized use, disctrubution or any adaptation of the code will result in ligal actions
#############################################################################################


#region ----------------------- Imports -------------------------
import matplotlib.pyplot as plt
import pandas as pd
#endregion

def PlotXY(data:pd.DataFrame,plotName:str="New plot"):
    
    plt.figure(figsize=(10, 6))
    plt.plot(data)
    
    plt.title('Plot')
    plt.xlabel('Index')
    plt.ylabel('Values')

    # Show the plot
    plt.show()