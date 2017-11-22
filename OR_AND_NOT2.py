import CONSTANTES as c
from CONJUNTOS import *

def caso(op):
    """ Es una funcion de orden superior que evalua <op> retornando una funcion correspondiente

        pre: la funcion [caso] solo tomara en cuenta las siguientes expresiones
            <or:>
            <and:>
            <not:>

        /*caso especial
        si <op> es diferente a [or: ,and:, not:] la funcion por defecto devolvera la funcion <OR>

        /*var
        op es un STR

        post: Devuelve una funcion

    """
    def OR_case(diccionario, terminos):
        """ Esta funcion muestra en pantalla las rutas que coinciden con los terminos

            pre: Esta funcion asume 2 estados
            /*explicita
            terminos[0] = "or:"

            /*implicita
            terminos[0] != "or:"

            /*var
            diccionario es un diccionario
            terminos es una lista
        """
        salto = True if op == c.OR else False

        #invariante
        lista_de_rutas = []

        for k in terminos:
            #salta primer termino si [OR:]
            if salto:
                salto = False
                continue

            if k.lower() in diccionario:
                agregar_rutas(lista_de_rutas, diccionario[k.lower()])

        if not lista_de_rutas:
            print(c.ERROR_COINCIDENCIAS)
            return

        for rutas in lista_de_rutas:
            print(rutas)
        return

    def NOT_case(diccionario, terminos):
        """ Esta funcion muestra en pantalla las rutas que no coinciden con el termino

            pre: el len(termino) == 2

            /*var
            diccionario es un diccionario

            terminos es una lista
        """
        if len(terminos) != 2:
            print(c.ERROR_NOT)
            return

        key_not = terminos[1].lower()
        lista_de_rutas = []

        if key_not not in diccionario:
            for k in diccionario:
                agregar_rutas(lista_de_rutas, diccionario[k])

            if not lista_de_rutas:
                print(c.ERROR_COINCIDENCIAS)
                return

            for rutas in lista_de_rutas:
                print(rutas)
            return

        for k in diccionario:
            if k == key_not:
                continue

            aux = calcular_diferencia(diccionario[k], diccionario[key_not])

            if not aux:
                continue

            agregar_rutas(lista_de_rutas, aux)


        if not lista_de_rutas:
            print(c.ERROR_COINCIDENCIAS)
            return

        for rutas in lista_de_rutas:
            print(rutas)
        return

    def AND_case(diccionario, terminos):
        """ Esta funcion muestra en pantalla las rutas que no coinciden con todos los terminos simultaneamente

            pre: el len(termino) > 2

            /*var
            diccionario es un diccionario

            terminos es una lista
        """
        if len(terminos)<3:
            print(c.ERROR_AND)
            return

        paso_checkeo = verifica_terminos(diccionario, terminos)

        if not paso_checkeo:
            print(c.ERROR_COINCIDENCIAS)
            return

        lista_de_rutas = []
        lista_terminos = cargar_terminos(terminos)

        aux = calcular_interseccion(diccionario, lista_terminos)
        agregar_rutas(lista_de_rutas, aux)

        if not lista_de_rutas:
            print(c.ERROR_COINCIDENCIAS)
            return

        for rutas in lista_de_rutas:
            print(rutas)
        return

    def QUIT_case(a=None, b=None):
        """retorna "quit" para salir de la aplicacion
        """
        return c.QUIT

    def VER_case(diccionario, b=None):
        """Muestra la lista_invertida = diccionario
            pre: diccionario es la lista_invertida
        """
        print()
        print("{:10}   {}".format("termino","rutas"))
        print()
        for k in diccionario:
            print("{:10}   {}".format(k,c.ESPACIO.join(diccionario[k])))
        print()
        return

    _case = {c.OR: OR_case,
             c.NOT: NOT_case,
             c.AND: AND_case,
             c.QUIT: QUIT_case, #salir del programa
             c.LISTA_INVERTIDA: VER_case # muestra lista invertida
                            }

    return _case.get(op,OR_case)
