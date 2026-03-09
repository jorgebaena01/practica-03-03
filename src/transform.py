# inicialmente voy a definir una clase que va a recibir el csv

import pandas as pd
class Transformador:
    
    def __init__(self,tabla):
        self.tabla=tabla

    def transform(self):
        x=pd.read_csv(self.tabla)
        x = x.dropna(subset=['date'])
        x['date']=pd.to_datetime(x['date'])
        return x
    

#x.to_csv('csv_fitlrado.csv', index=False)

w=Transformador('data/csv_clima.csv')
w.transform().to_csv('data/csv_fitlrado.csv', index=False)

print('se corrio el transform')