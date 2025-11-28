import numpy as np
from class_pila import Pila
from clase_arista import Arista

class Digrafo:
    __vertices:np.ndarray
    __dim:int

    def __init__(self,n):
        self.__vertices= np.empty(n,dtype=Arista)
        self.__dim= n

    def insertar(self, u,v,peso= 1):
        if not(0 <= u <= self.__dim) or not(0 <= v <= self.__dim):
            print('Error nodo invalido')
        else:
            arista= Arista(v,peso)
            arista.set_sig(self.__vertices[u])
            self.__vertices[u]= arista

    def recorrer_ad(self):
        for i in range(self.__dim):
            print(f'Vertice->{i+1}',end='-')
            aux= self.__vertices[i]
            while aux != None:
                print(f'Exites una arista al vertice->{aux.get_vertice()+1}')
                aux= aux.get_sig()


    def adyacentes(self,u):
        print(f'Vertice adyacente al vertice->{u+1}')
        for i in range(self.__dim):
            aux= self.__vertices[i]
            hallado = False
            while aux != None and not hallado:
                if aux.get_vertice() == u:
                    print(f'Vertice->{i+1}',end='-')
                    hallado= True
                else:
                    aux= aux.get_sig()
        return hallado

    def camino(self,u,v,camino,hallado= False, visitado=None):
        if visitado is None:
            visitados= [False]* self.__dim
        visitados[u]= True
        aux= self.__vertices[u]
        while aux is not None and not hallado:
            actual= aux.get_vertice()
            if not visitados[actual]:
                camino_actual= camino + actual
                f'{actual+1}'
                if actual==v:
                    hallado= True
                    print(f'Camino encotrado->{camino_actual}')
                else:
                    hallado= self.camino(actual,v,camino_actual,hallado,visitados)
            aux= aux.get_sig()
        return hallado
    
    def bep(self):
        pila= Pila()
        d= [0]*self.__dim
        f= [0]*self.__dim
        ciclo=[False]
        for s in range(self.__dim):
            if d[s] == 0:
                self.bep_visita(s, d, f, 0, ciclo, pila)

        return ciclo[0], pila
    
    def bep_visita(self, s,d, f, tiempo,ciclo, pila):
        tiempo += 1
        d[s]= tiempo
        aux= self.__vertices[s]
        while aux is not None:
            u= aux.get_vertice()
            if d[u] == 0:
                tiempo= self.bep_visita(u,d,f,tiempo,ciclo,pila)
            elif f[u] == 0:
                ciclo[0]= True
            aux= aux.get_sig()
        tiempo += 1
        f[s]= tiempo
        pila.insertar(s)
        return tiempo