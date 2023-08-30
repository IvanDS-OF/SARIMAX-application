# SARIMAX-application
Este programa genera un pronóstico usando el modelo SARIMAX.

This code generates a forecast using SARIMAX model.

## Pronóstico / Forecast

El pronóstico son datos futuros que han sido obtenidos mediante un procesamiento matemático.  

The forecast is future data that are obtained using a mathematical processing. 


Podemos encontrar el uso del pronóstico para obtener datos del tiempo, el clima, incluso las noticias tienen una sección del Pronóstico del tiempo, Igualmente, dentro de un ambiente más empresarial, podemos encontrar el uso del pronóstico para tener una idea de las ventas de un producto en una fecha determinada del año. También lo podemos encontrar para pronosticar el comportamiento de el uso de un servicio en la ciudad (viajes de trenes, vuelos, estancia en una cafetería, etc.)

## SARIMAX

SARMIAX significa **Seasonal AutoRegressive Integrated Moving Average with eXogenous regressors** que es Modelo Autorregresivo integrado de media móvil estacional con variables exógenas. Resumiendo, es un modelo que nos puede ofrecer un pronóstico de datos con datos previamente cargados, teniendo en cuenta para el resultado la tendencia, la estacionalidad de los datos, y la media. 

Podemos encontrar más información sobre el modelo en el siguiente [link](https://www.statsmodels.org/devel/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.html)

El uso de este modelo de predicción fue empleado para generar un pronóstico en el comportamiento de un proceso industrial, el cual no tenía un sistema de control con retroalimentación, por lo que al pasar el tiempo la variable observada cambiaba de tendencia y no se podía análizar de forma contínua, es por eso que se optó por un sistema de pronóstico para mantener una postura pro-activa en el control de la variable. 


## Código / Program

El programa comienza por importar las librerías necesarias para el funcionamiento del programa. Podemos encontrar entonces: 

```
import pandas as pd 		# To read the data from a .csv file
import numpy as np			# To generate some arrays
import matplotlib.pyplot as plt 	#To plotting
from statsmodels.tsa.statespace.sarimax import SARIMAX 	# THE MOST IMTPORTANT- This creates the forecasting data
import warnings 	# To ignore some warnings
warnings.filterwarnings("ignore")
```

Pra poder hacer uso de la librería para hacer el pronóstico podemos hacer uso del gestor de librerías PIP e instalarla con el siguiente comando: 

```
pip3 install statsmodels
```

> pip3 version == 23.2.1
> statsmodel version == 0.14.0
> setuptools version == 58.1.0

La primer función llamada _rango simple_ funciona para hacer un rango de los datos que son leídos, teniendo como argumentos los datos y el paso. Recordemos que el **Rango** es aquella función que evalúa un conjunto de datos y hace una resta del valor más grande y el más pequeño: 

$$
Range = maxValue - minValue
$$

Al ejecutar esta función y generar un histograma podremos ver un sesgo que tiene hacia el punto deseado, en el caso del ejemplo tenderán a 0. 

La segunda función llamada _media simple_ tiene como argumentos de entrada a dos argumentos, a los datos y al paso. Recordemos que la media ó promedio es la suma de todos los valores dados sobre la cantidad de valores dados. La función fué realizada con dos finalidades, hacer un suavizado simple de los datos y la reducción de los datos totales. El argumento _paso_ está dado para que la media tenga un comportmaiento móvil. 

Finalmente la función llamda _entrenamiento_ que contiene el uso del modelo de predicción SARIMAX. para hacer uso del modelo priero es necesario instalarlo e importarlo correctamente como se mencionó anteriormente. el comando para introducir los valores es: 

```
arima_model = SARIMAX(train_data, order=(1,1,1), seasonal_order=(1,1,1,12)
arima_result = arima_model.fit(disp=0)
forecast = arima_result.forecast(tiempos_futuros)
```

Otro aspecto importante de la función son los comandos de limpieza. Cada que se invoca a la función, los datos que son introducidos serán limpiados con el método **dropna()** de pandas. 

> Cuando se hace un sistema de predicción es recomendable separar todos los datos en 2, una de entrenamiento y otra de testeo, esto con la finalidad de encontrar los argumentos que se acomoden más a la información mediante el encuentro del _Error Cuadrático Medio_, pero en este caso el cliente solicitó que se utilizaran todos los datos posibles, buscando una mejor resolución del pronóstico. 

Siguiendo con el programa. Primero importamos uba base de datos _(la base de datos del ejemplo fue obtenida de un sensor analógico de forma manual.)_ Asignamos un vector de datos como datos de prueba y le asignaremos el nombre *prueba*. Aplicamos las 2 funciones previamente descritas (rango y media simples)y la función de entrenamiento. 

Finalmente ploteamos todo de forma que se puedan apreciar los valores con comandos de matplotlib. 

```
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
```









