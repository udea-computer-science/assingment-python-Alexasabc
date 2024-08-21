import pandas as pd
df = pd.read_csv('/workspaces/assingment-python-Alexasabc/assingment/data.csv', sep = "\t", header = None)
print(df)
with(open('data.csv', "r")) as file:
    data = file.readlines()
print (data)


