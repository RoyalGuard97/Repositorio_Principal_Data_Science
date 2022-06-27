from pandas import DateOffset


class Nodo():
    padre = None
    hijos = None
    dato = None
    coste = None

    #Función del Constructor
    def __init__(self,dato,hijos=None):
        self.hijos = None
        self.padre = None
        self.dato = dato
        self.asignar_hijos(hijos)
    
    #Obtener Datos
    def obtener_datos(self):
        return self.dato
    
    #Asignar Datos
    def asignar_datos(self,dato):
        self.dato = dato
    
    def obtener_coste(self):
        return self.coste
    
    def asignar_coste (self,coste):
        self.coste = coste
    
    #Asignar hijos
    def asignar_hijos(self,hijos):
        self.hijos = hijos
        if self.hijos != None:
            for hijito in self.hijos:
                hijito.padre = self
    
    #Obtener Hijos
    def obtener_hijos(self):
        return self.hijos
    
    #Obtener Padre
    def obtener_padre(self):
        return self.padre
    #Asignar padre
    def asignar_padre(self,padre):
        self.padre = padre
    
    def igual(self,nodo):
        if self.obtener_datos == nodo.obtener_datos():
            return True
        else:
            return False
    
    def en_lista(self,lista_nodos):
        en_la_lista = False
        for n in lista_nodos:
            if self.igual(n):
                en_la_lista = True
        return en_la_lista









 


