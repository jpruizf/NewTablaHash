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

    def set_clave(self,valor):
        self.__clave= valor
        
    def get_izq(self):
        return self.__izq
    
    def get_der(self):
        return self.__der
    
    def get_clave(self):
        return self.__clave
    
    def get_grado(self):
        grado= 0
        if self.__izq is not None:
            grado+= 1
        elif self.__der is not None:
            grado+= 1
        return grado