from clase_arbol import ABB


def test():
    a= ABB()
    a.set_raiz(a.insertar_claves(None,90))
    a.insertar_claves(a.get_raiz(),56)
    a.insertar_claves(a.get_raiz(),60)
    a.insertar_claves(a.get_raiz(),40)
    a.insertar_claves(a.get_raiz(),47)
    a.in_orden(a.get_raiz(),56)
    print(f'El nodo ingresado es hoja {a.hoja(60)}')
    '''print(f'Clave encontrada->{a.buscar_clave(a.get_raiz(),56).get_clave()}')
    a.pre_orden(a.get_raiz())
    #print(f'Elemento suprimido->{a.suprimir(a.get_raiz(),56).get_clave()}')
    print(f'\nEl elemento->{a.ascendente(a.get_raiz(),40,None).get_clave()} es padre ')
    print(f'El elemento->{a.hijo(a.get_raiz(),a.get_raiz().get_izq())} es hijo ')'''





if __name__ == '__main__':
    test()