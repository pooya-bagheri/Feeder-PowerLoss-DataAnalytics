# @author: Pooya Bagheri
import os 
import pandas as pd
from sqlalchemy import create_engine

ResultsDBfile='SimResultsIEEE123NodesCase2.db'

# a class is defined for loading data and covering the SQL and pivoting procedure:
class MLinputData: 
    #initialize the API with the database:
    DB = create_engine('sqlite:///'+os.path.abspath('')+'//'+ResultsDBfile, echo=False)     
    
    def __init__(self,FromDay,ToDay):
        RawVoltages=pd.read_sql_query('''
        select Instants.InstantID,Voltages.NodeID,Voltages.Vmag
        from Instants join Voltages on Instants.InstantID=Voltages.InstantID
        where Instants.Day>=%d and Instants.Day<=%d''' % (FromDay,ToDay),con=self.DB)
        Voltages=RawVoltages.pivot(index='InstantID', columns='NodeID', values='Vmag')
        self.x=Voltages.values
        Ploss=pd.read_sql_query('''
        select Losses.Ploss
        from Instants join Losses on Instants.InstantID=Losses.InstantID
        where Instants.Day>=%d and Instants.Day<=%d''' % (FromDay,ToDay),con=self.DB)
        self.y=Ploss.values
     
        