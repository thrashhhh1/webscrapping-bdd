import pandas as pd

data = pd.read_csv('partidosCampeonatoChileno.csv', header=0)

data_ = []

# Iterar sobre las filas del DataFrame
for index, row in data.iterrows():
    # Verificar si la columna 'Local' es igual a 'Concón National'
    if row['Local'] == 'Concón National':
        data_.append(row)

    if row['Visita'] == 'Concón National':
        data_.append(row)    

# Convertir data_ a un DataFrame si es necesario
filtered_data = pd.DataFrame(data_)

print(filtered_data)
