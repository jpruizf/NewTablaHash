from class_nodo import Nodo

class Pila:
    __cant:int
    __tope:Nodo

    def __init__(self):
        self.__tope= None
        self.__cant= 0

    def vacia(self):
        return self.__cant == 0
    
    def insertar(self,x):
        nodo= Nodo(x)
        if self.__tope == None:
            nodo.set_sig(self.__tope)
            self.__tope= nodo
            self.__cant+= 1


    def suprimir(self):
        if not self.vacia():
            aux= self.__tope
            self.__tope= self.__tope.get_sig()
            self.__cant-= 1
        else:
            print('Pila vacia')
        return aux
    
    def mostrar(self):
        aux= self.__tope
        while aux is not None:
            print(aux.get_dato())
            aux= aux.get_sig()