class Nodo:
    __dato:object
    __sig:object

    def __init__(self,d):
        self.__dato= d
        self.__sig= None

    def set_sig(self,nodo):
        self.__sig= nodo

    def get_sig(self):
        return self.__sig
    
    def get_dato(self):
        return self.__dato