import matplotlib.pyplot as plt
import pandas as pd

class Graficador:
    def __init__(self,entrada):
        self.entrada=entrada


    def grafica(self):
        data=pd.read_csv(self.entrada)
        data["date"] = pd.to_datetime(data["date"])

        date = data["date"]
        value = data["temperature_2m"]
        plt.figure(figsize=(10,5))
        plt.plot(date,value)

        plt.title("Temperature over Time")
        plt.xlabel("Date")
        plt.ylabel("Temperature (°C)")

        plt.xticks(rotation=45)

        plt.grid(True)

        plt.tight_layout()
        return plt.savefig('data/grafica_final.png')
    

w=Graficador('data/csv_fitlrado.csv')
w.grafica()

