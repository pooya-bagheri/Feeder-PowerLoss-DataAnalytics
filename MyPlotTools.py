#@author: Pooya

from matplotlib import pyplot as plt
import numpy as np

#class for plotting inside my analytic jupyter notebooks
class Plot():
    def __init__(self,plotHeight=5,plotWidth=6,FromDay=1,ToDay=1):
        plt.rcParams['figure.figsize'] = [plotHeight,plotWidth] #making the plots a bit larger than default size
        self.TimeAxisLimits(FromDay,ToDay)
    def TimeAxisLimits(self,FromDay,ToDay):
        self.FromDay=FromDay
        self.ToDay=ToDay
    def Compare(self,predicted,actual,title=None,legends=['Predicted', 'Actual'],yAxisLabel='Power Loss (kW)'):
        Times=np.linspace(self.FromDay-1,self.ToDay,predicted.shape[0])
        plt.plot(Times,predicted)
        plt.plot(Times,actual)
        if title:
            plt.title(title)
        plt.xlabel('Time (per day)')        
        plt.ylabel(yAxisLabel)
        plt.legend(legends, loc='upper left')
        plt.show()    
