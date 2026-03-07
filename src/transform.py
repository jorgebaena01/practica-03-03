# inicialmente voy a definir una clase que va a recibir el csv

class Transformador:
    def __init__(self,tabla):
        self.tabla=tabla

    def transform(self):
        x=pd.read_csv(self.tabla)
        x = x.dropna(subset=['date'])
        return x