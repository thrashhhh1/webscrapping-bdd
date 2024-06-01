import pandas as pd

data = pd.read_csv('partidosCampeonatoChileno.csv', header=0)

dataFiltred = []
dataArray = data.values.tolist()

for array in dataArray:
    if array[1] == 'Lautaro de Buin':
        dataFiltred.append(array)
    
print(dataFiltred)