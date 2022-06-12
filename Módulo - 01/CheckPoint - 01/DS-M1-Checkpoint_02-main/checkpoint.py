# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

from heapq import merge
import pandas as pd
import numpy as np

def Ret_Pregunta01():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "datasets/Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros cuya entidad sea Argentina retornando ese valor en un dato de tipo entero.
    Pista averiguar la funcion Shape
    '''
    #Tu código aca:
    tabla = pd.read_csv("datasets/Fuentes_Consumo_Energia.csv")
    return tabla.loc[tabla["Entity"] == "Argentina"].shape[0]

def Ret_Pregunta02():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "datasets/Fuentes_Consumo_Energia.csv".
    Esta función debe eliminar las columnas 'Code' y luego informar la cantidad de columnas
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    tabla = pd.read_csv("datasets/Fuentes_Consumo_Energia.csv")
    tabla.drop(columns= "Code",inplace=True)
    return len(tabla.columns)

def Ret_Pregunta03():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "datasets/Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros sin tener en cuenta aquellos con valores faltantes
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    tabla = pd.read_csv("datasets/Fuentes_Consumo_Energia.csv")
    indices = tabla[tabla["Code"].isna()].index
    return tabla.drop(indices).shape[0]

def Ret_Pregunta04():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "datasets/Fuentes_Consumo_Energia.csv".
    El ExaJulio es una unidad diferentes al TWh, es decir, no tiene sentido sumarlos o
    buscar proporciones entre ellos, la fórmula de conversión es:
    277.778 Teravatios/Hora (TWh) = 1 Exajulio
    Los campos terminados en "_EJ" corresponden a mediciones en Exajulios,
    y los terminados en "_TWh" corresponden a Teravatios/Hora.
    La consigna es crear un nuevo campo, que se denomine "Consumo_Total"
    y que guarde la sumatoria de todos los consumos expresados en Teravatios/Hora
    (convirtiendo a esta medida los que están en Exajulios)
    Esta función debe informar el consumo total para la entidad 'World' y año '2019',
    redondeado a 2 decimales (Ejemplo: 25.189 - > 25.19), retornando ese valor en un dato de tipo float.
    '''
    #Tu código aca:
    tabla = pd.read_csv("datasets/Fuentes_Consumo_Energia.csv")
    
    def función_de_conversión(valor):
        return valor*277.778

    tabla["Consumo_Total"] = tabla["Coal_Consumption_EJ"].apply(función_de_conversión) + tabla["Gas_Consumption_EJ"].apply(función_de_conversión) + tabla["Geo_Biomass_Other_TWh"] + tabla["Hydro_Generation_TWh"] + tabla["Nuclear_Generation_TWh"] + tabla["Solar_Generation_TWh"] + tabla["Wind_Generation_TWh"] + tabla["Oil_Consumption_EJ"].apply(función_de_conversión)
    resultado = tabla.loc[(tabla["Entity"] == "World") & (tabla["Year"] == 2019)]["Consumo_Total"][5189]
    return round(resultado,2)


def Ret_Pregunta05():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "datasets/Fuentes_Consumo_Energia.csv".
    Esta función debe informar el año de mayor generación de energía solar (Solar_Generation_TWh)
    para la entidad 'Europe' retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    tabla = pd.read_csv("datasets/Fuentes_Consumo_Energia.csv")
    valor = max(tabla.loc[tabla["Entity"] == "Europe"]["Solar_Generation_TWh"])
    return tabla.loc[tabla["Solar_Generation_TWh"] == valor]["Year"].values[0]

def Ret_Pregunta06(m1, m2):
    '''
    Esta función recibe dos array de Numpy de 2 dimensiones cada uno, y devuelve el valor booleano
    True si es posible realizar una multiplicación entre ambas matrices,
    y el valor booleano False si no lo es
    Ej:
        n1 = np.array([[0,0,0],[1,1,1],[2,2,2]])
        n2 = np.array([[3,3],[4,4],[5,5]])
        print(Ret_Pregunta06(n1,n2))
            True            -> Valor devuelto por la función en este ejemplo
        print(Ret_Pregunta06(n2,n1))
            False            -> Valor devuelto por la función en este ejemplo
    '''
    #Tu código aca:

    if m1.shape[1] == m2.shape[0]:
        return True
    else:
        return False
 

def Ret_Pregunta07():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "datasets/Fuentes_Consumo_Energia.csv".
    Esta función debe informar cuál de la siguiente lista de países tuvo mayor generacíon de
    energía solar (Solar_Generation_TWh) en el año 2019:
        * Argentina
        * Brazil
        * Chile
        * Colombia
        * Ecuador
        * Mexico
        * Peru
    Debe retornar el valor en un dato de tipo string.
    '''
    #Tu código aca:
    tabla = pd.read_csv("datasets/Fuentes_Consumo_Energia.csv")

    aux = tabla.loc[(tabla["Entity"] == "Argentina") | (tabla["Entity"] == "Brazil") | (tabla["Entity"] == "Chile") | (tabla["Entity"] == "Colombia") | (tabla["Entity"] == "Ecuador") | (tabla["Entity"] == "Mexico")|(tabla["Entity"] == "Peru")]

    return aux.loc[aux["Solar_Generation_TWh"] == max(aux["Solar_Generation_TWh"])].values[0][0]

def Ret_Pregunta08():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "datasets/Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de entidades diferentes que están presentes en el dataset
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    tabla = pd.read_csv("datasets/Fuentes_Consumo_Energia.csv")
    return tabla["Entity"].nunique()

def Ret_Pregunta09():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "datasets/Tabla1_ejercicio.csv" y "datasets/Tabla2_ejercicio.csv".
    Esta función debe informar el score promedio de los géneros femenino y masculino en formato tupla y redondeado a dos decimales:
    Ejemplo:    Si el score promedio femenino te da = 102.358 devolver 102.36
                Si el score promedio masculino te da = 102.023 devolver 102.02
    '''
    #Tu código aca:
    tabla1 = pd.read_csv("datasets/Tabla1_ejercicio.csv",sep=";")
    tabla2 = pd.read_csv("datasets/Tabla2_ejercicio.csv",sep=";")
    tabla_final = pd.merge(tabla1,tabla2)
    prom_m = tabla_final.loc[tabla_final["sexo"] == "F"]["score"].mean()
    prom_h = tabla_final.loc[tabla_final["sexo"] == "M"]["score"].mean()


    return round(prom_m,2),round(prom_h,2)


def Ret_Pregunta10(lista):
    '''
    Esta función recibe como parámetro un objeto de la clase Lista() definida en el archivo Lista.py.
    Debe recorrer la lista y retornan la cantidad de nodos que posee. Utilizar el método de la clase
    Lista llamado getCabecera()
    Ejemplo:
        lis = Lista()
        lista.agregarElemento(1)
        lista.agregarElemento(2)
        lista.agregarElemento(3)
        print(Ret_Pregunta10(lista))
            3    -> Debe ser el valor devuelto por la función Ret_Pregunta10() en este ejemplo
    '''
    #Tu código aca:
    from Lista import Lista
    if (lista.getCabecera() == None):
            return 0
    else:
        contador = 1
        puntero = lista.getCabecera()
        while(puntero.getSiguiente() != None):
                contador += 1
                puntero = puntero.getSiguiente()
        return contador


