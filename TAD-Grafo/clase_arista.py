class Arista:
    __vertice:object
    __peso:int
    __sig:object

    def __init__(self,v,p):
        self.__vertice= v
        self.__peso=p
        self.__sig= None

    def set_sig(self,nodo):
        self.__sig= nodo

    def get_sig(self):
        return self.__sig
    
    def get_vertice(self):
        return self.__vertice
    
    def get_peso(self):
        return self.__peso