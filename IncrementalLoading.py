# @author: Pooya

from LoadingDataClass import MLinputData
from sklearn.preprocessing import StandardScaler

#a class defined to realize data generator object for incremental training in Keras
class DataGenerator():
    def __init__(self, FromDay,ToDay,DaysPerChunk):
        self.FromDay=FromDay
        self.ToDay=ToDay
        self.DaysPerChunk=DaysPerChunk
        self.DayNo=self.FromDay
        self.LastLoadedDay=None #for initialization purpose
        self.LoadScaleDataChunk() #loading the first chunk of data and initialize scaling
        
    def LoadScaleDataChunk(self):
        if self.LastLoadedDay==None or self.LastLoadedDay==self.ToDay:
            d0=self.FromDay          
        else:
            d0=self.LastLoadedDay+1
        d1=min(d0+self.DaysPerChunk,self.ToDay)    
        DataChunk=MLinputData(d0,d1) #uses an instant of MLinputData to load one full day of data using SQL queries written inside this class
        #Scaling the data
        if not hasattr(self,'scaler_x'): #if called for first-time, initialize scaler
            self.scaler_x=StandardScaler()
            self.xData=self.scaler_x.fit_transform(DataChunk.x)
            self.scaler_y=StandardScaler()
            self.yData=self.scaler_y.fit_transform(DataChunk.y)
        else:
            self.xData=self.scaler_x.transform(DataChunk.x)
            self.yData=self.scaler_y.transform(DataChunk.y)
        self.LastLoadedDay=d1 
        
    def __iter__(self,BatchSize):
        self.BatchPointer=None
        self.BatchSize=BatchSize
        return self
    
    def BatchEndPointer(self):
        return min(self.BatchPointer+self.BatchSize,self.xData.shape[0])
     
    def __next__(self):
        if self.BatchPointer==None: 
            self.BatchPointer=0
        elif self.BatchEndPointer()==self.xData.shape[0]:
            self.BatchPointer=0
            self.LoadScaleDataChunk()
        else:
            self.BatchPointer += self.BatchSize
        Range=(self.BatchPointer,self.BatchEndPointer())
        return (self.xData[Range[0]:Range[1],:],self.yData[Range[0]:Range[1]])

