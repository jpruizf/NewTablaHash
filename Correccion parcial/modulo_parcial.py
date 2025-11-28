class Nodo:
    __clave:object
    __izq:object
    __der:object

    def __init__(self,valor):
        self.__clave= valor
        self.__izq= None
        self.__der= None

    def set_izq(self,nodo):
        self.__izq= nodo
    
    def set_der(self,nodo):
        self.__der= nodo

    def get_izq(self):
        return self.__izq
    
    def get_der(self):
        return self.__der
    
    def get_clave(self):
        return self.__clave
    

class ABB:
    __raiz:Nodo

    def __init__(self):
        self.__raiz= None

    def set_raiz(self,nodo):
        self.__raiz= nodo
    
    def get_raiz(self):
        return self.__raiz
    
    def insertar_claves(self,r,c):
        if r is None:
            r= Nodo(c)
        elif r.get_clave() > c:
            r.set_izq(self.insertar_claves(r.get_izq(),c))
        elif r.get_clave() < c:
            r.set_der(self.insertar_claves(r.get_der(),c))
        return r
    
    def hoja(self,r,n):
        if r is not None:
            self.hoja(r.get_izq(),n)
            if n <= r.get_clave() and r.get_izq() is None or r.get_der() is None:
                print(f'Nodos terminales->{r.get_clave()}')
            self.hoja(r.get_der(),n)
'''-----------------Algoritmo correcto-------------------------'''
import numpy as np

class Digrafo:
    __matriz:np.ndarray
    __dim:int
    __peso:int

    def __init__(self,n):
        self.__dim= n
        self.__matriz= np.zeros((self.__dim,self.__dim),dtype=int)
        self.__peso= 0
    
    def insrtar_vertices(self,u,v,peso): #U es origen | V es destino 
        if not(0 <= u <= self.__dim) or not(0 <= v <= self.__dim):
            raise ValueError('Error nodo no valido')
        else:
            self.__matriz[u][v]= peso

    def adyacentes(self,nodo):
        for i in range(self.__dim):
            if self.__matriz[nodo][i] > 1:
                print(f'Vertice {nodo} es adyacente a {i+1}')
            else:
                print('El nodo ingresado no tiene adyacentes')
'''------------->    Corregido ** Algoritmo incorreco** observacion-> rehacer algoritmo y prestar atencional al contenido de las variables   <-------------------'''
import numpy as np
import random
class TablaHash:
    __tabla:np.ndarray
    __dim:int
    def __init__(self,n):
        self.__dim=round(n/0.7)
        self.__tabla= np.empty(self.__dim,dtype=object)
    def dimension(self):
        print(self.__dim)
    def funcion_hash(self,valor):
        k= valor//10**5
        return k%self.__dim

    def insertar_clave(self,clave):
        dir= int(self.funcion_hash(clave))
        print(dir)
        c= 0
        while c < self.__dim and self.__tabla[dir] is not None:
            c+= 1
            dir= (dir+1)%self.__dim
            if c== self.__dim:
                print('Tabla llena')
                return None
            self.__tabla[dir]= clave
        return self.__tabla[dir]
    
if __name__ == '__main__':
    tb=TablaHash(500)
    tb.dimension()
    print(f'Clave insertada->{tb.insertar_clave(654321)}')
    '''g=Digrafo(5)
    g.insrtar_vertices(1,1,1)
    g.insrtar_vertices(2,3,1)
    g.insrtar_vertices(3,2,0)
    g.insrtar_vertices(2,1,1)
    g.insrtar_vertices(3,1,1)
    g.adyacentes(1)
    g.adyacentes(3)'''
    '''arbol= ABB()
    arbol.set_raiz(arbol.insertar_claves(None,80))
    arbol.insertar_claves(arbol.get_raiz(),50)
    arbol.insertar_claves(arbol.get_raiz(),20)
    arbol.insertar_claves(arbol.get_raiz(),40)
    arbol.insertar_claves(arbol.get_raiz(),60)
    arbol.hoja(arbol.get_raiz(),50)'''