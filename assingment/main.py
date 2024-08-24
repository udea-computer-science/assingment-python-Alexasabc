
'''
Base de datos
Importamos la libreria pandas para la manipulación de datos
'''
import pandas as pd

#Cargamos la base de datos csv

datos = pd.read_csv('/workspaces/assingment-python-Alexasabc/assingment/data.csv', sep = "\t", header = None)
df = pd.DataFrame(datos, columns=None)

'''
Imprima la suma de la segunda columna de la base de datos
'''
#La llamamos a traves del indice
print("MANIPULACION DE DATOS")
print("-"*70)
print("La suma de la segunda columna es ", df[1].sum())
print("-"*70)

'''
Imprima la cantidad de registros por letra para la primera columna, ordenados alfabeticamente.
'''
#Agrupamos la columna con indice 0, y le agregamos el conteo de la columna con indice 1.
print("Cantidad de registros por letra para la primera columna")
print(df.groupby([0]).agg({1: 'count'}))
print("-"*70)

'''
Imprima la suma de la columna 2 por cada letra de la primera columna,
ordneados alfabeticamente.
'''
#Agrupamos la columna con indice 0, y le agregamos la suma de la columna con indice 1.
print("Suma de la columna 2 por cada letra de la primera columna")
print(df.groupby([0]).agg({1: "sum"}))
print("-"*70)








