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




