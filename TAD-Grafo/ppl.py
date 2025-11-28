from clase_digrafo import Digrafo

def test():
    g= Digrafo(5)
    g.insertar(1,1,1)
    g.insertar(1,2,1)
    g.insertar(3,1,0)
    g.insertar(4,0,1)
    g.insertar(0,2,1)
    g.recorrer_ad()
    g.adyacentes(3)
    print(g.camino(1,2,0,False,None))




if __name__ == '__main__':
    test()