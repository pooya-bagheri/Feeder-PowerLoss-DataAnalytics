#@author: Pooya

from matplotlib import pyplot as plt
import numpy as np
from sklearn.metrics import mean_absolute_error

#class for plotting inside my analytic jupyter notebooks
class Plot():
    def __init__(self,plotHeight=5,plotWidth=6,FromDay=1,ToDay=1):
        plt.rcParams['figure.figsize'] = [plotWidth,plotHeight] #making the plots a bit larger than default size
        self.TimeAxisLimits(FromDay,ToDay)
    
    def TimeAxisLimits(self,FromDay,ToDay):
        self.FromDay=FromDay
        self.ToDay=ToDay
    
    def GenTimeAxis(self,Y):    
        self.Times=np.linspace(self.FromDay-1,self.ToDay,Y.shape[0])
    
    def Core(self,Y,yAxisLabel='Power Loss (kW)',title=None):
        self.GenTimeAxis(Y)
        plt.plot(self.Times,Y)
        if title:
            plt.title(title)
        plt.xlabel('Measurement Time (per day)')        
        plt.ylabel(yAxisLabel)
    
    def Single(self,Y,yAxisLabel='Power Loss (kW)',title=None):        
        self.Core(Y,yAxisLabel,title)
        plt.show()
    
    def Multiple(self,Ylist,TitleList,yAxisLabels,subplotbase=210):
        i=1
        for Y,yAxisLabel,title in zip(Ylist,yAxisLabels,TitleList):
            plt.subplot(subplotbase+i)
            self.Core(Y=Y,yAxisLabel=yAxisLabel,title=title)
            i+=1
        plt.show()
    
    def Compare(self,predicted,actual,title=None,legends=['Predicted', 'Actual'],yAxisLabel='Power Loss (kW)',legendloc='upper center'):
        self.GenTimeAxis(predicted)
        plt.plot(self.Times,predicted)
        plt.plot(self.Times,actual)
        if title:
            plt.title(title)
        plt.xlabel('Measurement Time (per day)')        
        plt.ylabel(yAxisLabel)
        plt.legend(legends, loc=legendloc)
        plt.show()    
    
    def AssessPrediction(self,predicted,actual,IsTrainSet=False): 
        MAE=mean_absolute_error(actual,predicted)
        if IsTrainSet:
            SetName='Training'
        else:
            SetName='Test'
        PltTitle='Average prediction error on %s set is %.1f%%' % (SetName,MAE/actual.mean()*100)
        self.Compare(predicted,actual,title=PltTitle)
     
    @staticmethod
    def LearningCurve(History):
        plt.plot(History.history['loss'])
        plt.plot(History.history['val_loss'])
        plt.title('Model loss')
        plt.ylabel('Loss')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Test'], loc='upper left')
        plt.show()
            
        