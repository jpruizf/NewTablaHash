from clase_nodo import Nodo

class ABB:
    __raiz:Nodo

    def __init__(self):
        self.__raiz= None

    def get_raiz(self):
        return self.__raiz
    
    def set_raiz(self,valor):
        self.__raiz= valor
    
    def insertar_claves(self,r,c):
        if r is None:
            r= Nodo(c)
        elif r.get_clave() > c:
            r.set_izq(self.insertar_claves(r.get_izq(),c))
        elif r.get_clave() < c:
            r.set_der(self.insertar_claves(r.get_der(),c))
        return r

    def buscar_clave(self,r,c):
        if r == None:
            raise RecursionError('Error Arbol vacio')
        else:
            if c == r.get_clave():
                retorno= r
            elif c < r.get_clave():
                retorno= self.buscar_clave(r.get_izq(),c)
            else:
                retorno= self.buscar_clave(r.get_der(),c)
        return retorno
    
    def ascendente(self,r,c,padre=None):
        aux= None
        if r is not None:
            if r.get_clave() == c:
                aux= padre
            elif r.get_clave() < c:
                aux= self.ascendente(r.get_der(),c,r)
            else:
                aux= self.ascendente(r.get_izq(),c,r)
        return aux
    def hijo(self,r,c):
        return r.get_izq() == c or r.get_der() == c

    def padre(self,r,c):
        return r.get_izq() == c or r.get_der() == c
    
    def hoja(self,c):
        return self.buscar_clave(self.get_raiz(),c).get_grado() == 0
    def pre_orden(self,r):
        if r is not None:
            print(f'{r.get_clave()}',end='- ')
            self.pre_orden(r.get_izq())
            self.pre_orden(r.get_der())
    def in_orden(self,r,c):
        if r is not None:
            self.in_orden(r.get_izq(),c)
            if r.get_clave() <= c:
                print(f'{r.get_clave()}',end='-')
            self.in_orden(r.get_der(),c)
    def maximo_izq(self,padre,raiz):
        if raiz.get_der() is not None:
            padre= raiz
            self.maximo_izq(raiz.get_der(),padre)
        else:
            return raiz,padre
            
    def suprimir(self,r,c):
        nuevo= r
        if r == None:
            raise RecursionError('ERROR ARBOL VACIO')
        else:
            if r.get_clave() > c:
                r.set_izq(self.suprimir(r.get_izq(),c))
            elif r.get_clave() < c:
                r.set_der(self.suprimir(r.get_der(),c))
            else:
                if r.get_grado() == 0:
                    nuevo = None
                elif r.get_grado() == 1:
                    nuevo= r.get_der() if r.get_der() is not None else r.get_izq()
                
                else:
                    ant= None
                    maximo= r.get_izq()
                    while maximo.get_der() is not None:
                        ant= maximo
                        maximo= maximo.get_der()
                    r.set_clave(maximo.get_dato())
                    ant.set_der(maximo.get_izq())
        return nuevo