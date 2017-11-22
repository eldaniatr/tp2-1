#Leonel R. Rolon
#padron 101009
#Facultad de Ingenieria Universidad de Buenos Aires

import OR_AND_NOT2 as obtener
import RUN_DIRECTORIOS3 as loading
import os as SO
import re
import CONSTANTES as c

def cmd(lista_invertida):
    """ Emula una lista de comandos:
        los comandos son:
        <or:> <termino1>..<terminoN>
        <and:> <termino>..<terminoN>
        <not:> <termino>
        pre: Para los operadores OR,AND,NOT siempre va acompañado del caracter :
            en caso de no poseerlo se tomara la entrada como un caso OR

        /*var
        lista_invertida es un diccionario
    """
    try:
        argumentos= input(c.PROMPT).split()
        tipo_de_caso = argumentos[0].lower()
    except IndexError:
        print(c.ERROR_PROMPT)
        return

    busqueda = obtener.caso(tipo_de_caso)
    return busqueda(lista_invertida, argumentos)

#Funcion main()
def loopCMD(lista_invertida):
    """ Mantiene el programa Activo
        pre:
        /* var
        lista_invertida es un diccionario
    """
    while True:
        status = cmd(lista_invertida)
        if status == c.QUIT:
            break

#---------------------------------------------------------------------
#recorre los directorios y los indexa
cantidad_archivos,lista_invertida = loading.recorrer_arbol_directorios()

print("Archivos INDEXADOS: ",cantidad_archivos)

#comienza el programa
loopCMD(lista_invertida)
