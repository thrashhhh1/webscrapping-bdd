import pandas as pd
import xml.etree.ElementTree as ET

data = pd.read_csv('partidosCampeonatoChileno.csv', header=0)

dataFiltred = []
dataArray = data.values.tolist()
toSearch = 'Trasandino'

dataFiltred = [array for array in dataArray if array[2] == toSearch or array[4] == toSearch]

def invertir_numeros(cadena):
    partes = cadena.split()
    partes_invertidas = partes[::-1]
    return '-'.join(partes_invertidas)

def formatear_numeros(cadena):
    partes = cadena.split()
    return '-'.join(partes)

def toxml(dataFiltred):
    dataMerge = []

    for array in dataFiltred:
        if array[2] == toSearch:
            if isinstance(array[3], str):
                array[3] = formatear_numeros(array[3])
            array.append('local')  # Añadir "local" en la posición [6]
            dataMerge.append(array)
            #hazlo aca
        else:
            array[2], array[4] = array[4], array[2]
            if isinstance(array[3], str):
                array[3] = invertir_numeros(array[3])
            array.append('visita')  # Añadir "visita" en la posición [6]
            dataMerge.append(array)
        #hazlo aca 2

    root = ET.Element('equipo')
    name_ = ET.SubElement(root, 'nombre')
    name_.text = toSearch
    partidos = ET.SubElement(root, 'partidos')

    for array in dataMerge:
        partido = ET.SubElement(partidos, 'partido')

        fecha = ET.SubElement(partido, 'fecha')
        fecha.text = array[0]

        hora = ET.SubElement(partido, 'hora')
        hora.text = array[1]

        resultado = ET.SubElement(partido, 'resultado')
        resultado.text = array[3]

        oponente = ET.SubElement(partido, 'oponente')
        oponente.text = array[4]

        estadio = ET.SubElement(partido, 'estadio')
        estadio.text = array[5]

        modalidad = ET.SubElement(partido, 'modalidad')
        modalidad.text = array[6]

    # Crear el árbol XML y escribirlo en un archivo
    tree = ET.ElementTree(root)
    with open('file.xml', 'wb') as file:
        tree.write(file, encoding='utf-8', xml_declaration=True)

toxml(dataFiltred)
