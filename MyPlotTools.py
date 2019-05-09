#@author: Pooya

from matplotlib import pyplot as plt
import numpy as np

#class for plotting inside my analytic jupyter notebooks
class Plot:
    def __init__(self,plotHeight=5,plotWidth=6,FromDay=1,ToDay=1):
        self.plt=plt
        self.plt.rcParams['figure.figsize'] = [plotHeight,plotWidth] #making the plots a bit larger than default size
        self.TimeAxisLimits(FromDay,ToDay)
    def TimeAxisLimits(self,FromDay,ToDay):
        self.FromDay=FromDay
        self.ToDay=ToDay
    def Compare(self,predicted,actual,title=None,legends=['Predicted', 'Actual'],yLabel='Power Loss (kW)'):
        Times=np.linspace(self.FromDay-1,self.ToDay,predicted.shape[0])
        self.plt.plot(Times,predicted)
        self.plt.plot(Times,actual)
        if title:
            self.plt.title(title)
        plt.xlabel('Time (per day)')
        plt.ylabel()
        self.plt.legend(legends, loc='upper left')
        self.plt.show()    
