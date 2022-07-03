from imp import source_from_cache
from weakref import WeakValueDictionary
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup as bs
import numpy as np

def funcion_scrapy_mercado_libre(cadena,nombre_archivo):
    driver = webdriver.Chrome("D:\DataScience\Yakomo\Web Scraping\chromedriver_win32\chromedriver.exe")
    paginaScrapy = cadena
    driver.get(paginaScrapy)
    contenido = driver.page_source
    soup = bs(contenido)

    #Obtención de Datos
    nombre_juegos_sucio = []
    precio_juegos_sucio = []
    vendedor_juegos_sucio = []
    envio_gratis_sucio = []
    oferta_situacion_sucio = []

    for tarjeta in soup.find_all("div",attrs={"class":"ui-search-result__content-wrapper"}):
        #Se Obtiene el Nombre del Producto
        datos_nom = tarjeta.find("h2",attrs={"class":"ui-search-item__title"})
        nombre_juegos_sucio.append(datos_nom.text)
        #Se Obtiene el Precio Original del Producto
        datos_precio = tarjeta.find("span",attrs={"class":"price-tag-fraction"})
        precio_juegos_sucio.append(datos_precio.text)
        #Se obtiene la entidad que lo vende
        datos_vendedor = tarjeta.find("a",attrs={"class":"ui-search-official-store-item__link ui-search-link"})
        if(datos_vendedor==None):
            vendedor_juegos_sucio.append(np.nan)
        else:
            vendedor_juegos_sucio.append(datos_vendedor.text)
        #Nos dice si el envío gratis se encuentra disponible o no. 
        datos_envio = tarjeta.find("p",attrs={"class":"ui-search-item__shipping ui-search-item__shipping--free"})
        if(datos_envio == None):
            envio_gratis_sucio.append(0)
        else:
            envio_gratis_sucio.append(1)
        
        #Nos dice si el producto está bajo una determinada oferta
        datos_oferta = tarjeta.find("span",attrs={"class":"ui-search-price__discount"})
        if(datos_oferta==None):
            oferta_situacion_sucio.append(0)
        else:
            oferta_situacion_sucio.append(1)

    #Creamos un diccionario
    dicc = dict(producto=nombre_juegos_sucio,precio_original=precio_juegos_sucio,vendedor=vendedor_juegos_sucio,envio_gratis = envio_gratis_sucio,oferta=oferta_situacion_sucio)
    #Creamos un Dataframe
    df = pd.DataFrame(dicc)

    #Definimos una funcion para alterar el dato vendedor
    def funcion_vendedor(elemento):
        if type(elemento) == str:
            return elemento
        else:
            return elemento

    df["vendedor"] = df["vendedor"].apply(funcion_vendedor)
    df["precio_original"] = df["precio_original"].astype(float)
    df.to_csv(nombre_archivo,index=False)