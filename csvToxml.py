import pandas as pd

data = pd.read_csv('partidosCampeonatoChileno.csv', header=0)

dataFiltred = []
dataArray = data.values.tolist()

dataFiltred = [array for array in dataArray if array[1] == 'Lautaro de Buin' or array[3] == 'Lautaro de Buin']

def invertir_numeros(cadena):
    partes = cadena.split()
    partes_invertidas = partes[::-1]
    return ' '.join(partes_invertidas)


def toxml(dataFiltred):
    dataMerge = []
    xml = []

    for array in dataFiltred:
        if array[1] == 'Lautaro de Buin':
            dataMerge.append(array)
        else:
            array[1], array[3] = array[3], array[1]
            if isinstance(array[2], str):
                array[2] = invertir_numeros(array[2])
                dataMerge.append(array)

    for xml in dataMerge:
        xml.append(f"<fecha>{dataMerge[0]}</fecha>\n<oponente>{dataMerge[4]}</oponente>\n<resultado>{dataMerge[3]}</resultado>\n<estadio>{dataMerge[5]}</estadio>\n")


    
    output_file = 'CampeonatoChileno.xml'
    with open(output_file, 'a', encoding='utf-8') as file:
        for item in xml:
            file.write(item)
                


toxml(dataFiltred)