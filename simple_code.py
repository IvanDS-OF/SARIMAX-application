# Primero colocamos las librerías necesarias para el programa
# First at all, write the needed libraries

import pandas as pd 		# To read the data from a .csv file
import numpy as np			# To generate some arrays
import matplotlib.pyplot as plt 	#To plotting
from statsmodels.tsa.statespace.sarimax import SARIMAX 	# THE MOST IMTPORTANT- This creates the forecasting data
import warnings 	# To ignore some warnings
warnings.filterwarnings("ignore")



# Esta función sirvve para hacer un rango de los datos. 
def rangoSimple (datos, paso):
    vector = []
    sss = []
    for i in range(datos.index.values[0], datos.index.values[len(datos)-1]):
        s = datos
        vector.append(s[i])
        if len(vector) == paso:
            v = max(vector) - min(vector)
            sss.append(v)
            vector = []
    return sss


def mediaSimple (datos, paso):
    vector = []
    sss = []
    for i in range(datos.index.values[0], datos.index.values[len(datos)-1]):
        s = datos
        vector.append(s[i])
       
        if len(vector) == paso:
            v = np.mean(vector)
            sss.append(v)
            vector = []
    
    return sss


def entrenamiento(dato1, tiempos_futuros = 20):
	df1 = pd.DataFrame(dato1)
	df1 = df1.dropna()
	train_data = df1
	#arima_model = SARIMAX(train_data, order = (2,1,3), seasonal_order = (2,1,4,65))
	arima_model = SARIMAX(train_data, order=(1,1,1), seasonal_order=(1,1,1,5), enforce_stationarity=False, enforce_invertibility=False)
	arima_result = arima_model.fit(disp=0)
	fc = arima_result.forecast(tiempos_futuros)  # 95% conf
	return fc



# Leemos la base de datos:
# Read the data base and create a Pandas Dataframe
df = pd.read_csv("Data.csv")

prueba = df["UNO"]



prueba_r = rangoSimple(prueba, paso = 10)
prueba_m = mediaSimple(prueba, paso = 5)

entrenamiento = entrenamiento(prueba, tiempos_futuros = 30)


plt.title("prueba")

plt.plot(np.linspace(0, 400, len(prueba)), prueba, c="0.7", label="Dato Real") 
plt.plot(np.linspace(0, 400, len(prueba_r)), np.array(prueba_r)+1, c="b", label="Rango de dato Real") #Rango
plt.plot(np.linspace(0, 400, len(prueba_m)), np.array(prueba_m), c="k", label="Media de dato Real") #Media
plt.plot(np.linspace(400, 430, len(entrenamiento)), entrenamiento, c="m", label="Pronóstico")
plt.legend(loc='lower left', fontsize=18)

plt.grid()

plt.show()




print("Merci pour votre atention :D")





















