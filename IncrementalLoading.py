# @author: Pooya

from LoadingDataClass import MLinputData
from sklearn.preprocessing import StandardScaler

#a class defined to realize data generator object for incremental training in Keras
class DataGenerator():
    def __init__(self, FromDay,ToDay):
        self.FromDay=FromDay
        self.ToDay=ToDay
        self.DayNo=self.FromDay
        self.LoadScaleDataChunk() #loading the first chunk of data and initialize scaling
        
    def LoadScaleDataChunk(self):
        DataChunk=MLinputData(self.DayNo,self.DayNo) #uses an instant of MLinputData to load one full day of data using SQL queries written inside this class
        #Scaling the data
        if not hasattr(self,'scaler_x'): #if called for first-time, initialize scaler
            self.scaler_x=StandardScaler()
            self.xData=self.scaler_x.fit_transform(DataChunk.x)
            self.scaler_y=StandardScaler()
            self.yData=self.scaler_y.fit_transform(DataChunk.y)
        else:
            self.xData=self.scaler_x.transform(DataChunk.x)
            self.yData=self.scaler_y.transform(DataChunk.y)
            
    def __iter__(self,BatchSize):
        self.BatchNo = 0
        self.DayNo=self.FromDay
        self.BatchSize=BatchSize
        self.BatchPerDay=1440/self.BatchSize
        assert self.BatchPerDay % 1 == 0
        return self
       
    def __next__(self):
        self.BatchNo+=1
        if self.BatchNo > self.BatchPerDay:
            self.BatchNo=1
            self.DayNo+=1
            if self.DayNo > self.ToDay:
                self.DayNo=self.FromDay
            self.LoadScaleDataChunk()
        Range=((self.BatchNo-1)*self.BatchSize,self.BatchNo*self.BatchSize)
        return (self.xData[Range[0]:Range[1],:],self.yData[Range[0]:Range[1]])
