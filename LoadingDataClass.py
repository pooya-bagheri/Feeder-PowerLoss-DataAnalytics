# @author: Pooya Bagheri
import os 
import pandas as pd
from sqlalchemy import create_engine
# a class is defined for loading data and covering the SQL and pivoting procedure:
class MLinputData:
    DB=None #SQL database only needs to be initialized for the whole class once 
    def __init__(self,FromDay,ToDay):
        if self.DB is None: #Ensures to initialize SQL database as soon as the first instance of class is created
            DBfilePath=os.path.abspath('')+'//'+'SimResultsIEEE123NodesCase2.db'
            self.DB = create_engine('sqlite:///'+DBfilePath, echo=False)   
        RawVoltages=pd.read_sql_query('''
        select Instants.InstantID,Voltages.NodeID,Voltages.Vmag
        from Instants join Voltages on Instants.InstantID=Voltages.InstantID
        where Instants.Day>=%d and Instants.Day<=%d''' % (FromDay,ToDay),con=self.DB)
        Voltages=RawVoltages.pivot(index='InstantID', columns='NodeID', values='Vmag')
        self.x=Voltages.values
        """
        Ploss=pd.read_sql_query('''
        select Losses.Ploss
        from Instants join Losses on Instants.InstantID=Losses.InstantID
        where Instants.Day>=%d and Instants.Day<=%d''',% (FromDay,ToDay),con=self.DB)
        self.y=Ploss.values
        """
        