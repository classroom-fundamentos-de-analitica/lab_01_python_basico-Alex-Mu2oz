"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

import csv  # Librería para leer archivos CSV   
def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma = 0
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            suma += int(row[1])
    return suma
   


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        letras = [row[0] for row in reader]
        letras = sorted(letras)
        letras_unicas = list(set(letras))
        cantidad = []
        for letra in letras_unicas:
            cantidad.append((letra, letras.count(letra)))
    return cantidad


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        letras = [row[0] for row in reader]
        file.seek(0)
        valores = [int(row[1]) for row in reader]
        letras_unicas = list(set(letras))
        suma = []
        for letra in letras_unicas:
            suma.append((letra, sum([valores[i] for i in range(len(letras)) if letras[i] == letra])))
    return suma
    

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        fechas = [row[2] for row in reader]
        meses = [fecha[5:7] for fecha in fechas]
        meses_unicos = list(set(meses))
        cantidad = []
        for mes in meses_unicos:
            cantidad.append((mes, meses.count(mes)))
    return cantidad


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        letras = [row[0] for row in reader]
        file.seek(0)
        valores = [int(row[1]) for row in reader]
        letras_unicas = list(set(letras))
        max_min = []
        for letra in letras_unicas:
            max_min.append((letra, max([valores[i] for i in range(len(letras)) if letras[i] == letra]), min([valores[i] for i in range(len(letras)) if letras[i] == letra])))
    return max_min
    


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        claves = [row[4] for row in reader]
        claves = [clave.split(":") for clave in claves]
        claves_unicas = list(set([clave[0] for clave in claves]))
        valores = [int(clave[1]) for clave in claves]
        max_min = []
        for clave in claves_unicas:
            valores_clave = [int(clave[1]) for clave in claves if clave[0] == clave]
            max_min.append((clave, min(valores_clave), max(valores_clave)))
    return max_min



def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]
    """
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        column0 = [int(row[0]) for row in reader]
        file.seek(0)
        column1 = [row[1] for row in reader]
        unique_values = list(set(column0))
        result = []
        for value in unique_values:
            associated_letters = [column1[i] for i in range(len(column0)) if column0[i] == value]
            result.append((value, associated_letters))
    return result



def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        column1 = [int(row[1]) for row in reader]
        file.seek(0)
        column0 = [row[0] for row in reader]
        unique_values = list(set(column1))
        result = []
        for value in unique_values:
            associated_letters = sorted(list(set([column0[i] for i in range(len(column1)) if column1[i] == value])))
            result.append((value, associated_letters))
    return result


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        claves = [row[4] for row in reader]
        claves = [clave.split(":")[0] for clave in claves]
        claves_unicas = list(set(claves))
        cantidad = {}
        for clave in claves_unicas:
            cantidad[clave] = claves.count(clave)
    return cantidad
    


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        column0 = [row[0] for row in reader]
        file.seek(0)
        column4 = [row[3] for row in reader]
        file.seek(0)
        column5 = [row[4] for row in reader]
        result = []
        for i in range(len(column0)):
            result.append((column0[i], len(column4[i]), len(column5[i].split(":"))))
    return result
    

import csv  # Librería para leer archivos CSV
def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        column3 = [row[3] for row in reader]
        file.seek(0)
        column1 = [int(row[1]) for row in reader]
        unique_values = list(set(column3))
        result = {}
        for value in unique_values:
            result[value] = sum([column1[i] for i in range(len(column3)) if column3[i] == value])
    return result
    


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        column0 = [row[0] for row in reader]
        file.seek(0)
        column4 = [row[3] for row in reader]
        result = {}
        for value in list(set(column0)):
            result[value] = sum([len(column4[i].split(":")) for i in range(len(column0)) if column0[i] == value])
    return result
