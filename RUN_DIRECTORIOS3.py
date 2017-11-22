import os as SO
import re
import CONSTANTES as c

def evita_duplicado(diccionario, termino, ruta):
    """ Chequea que el [path] en el diccionario para evitar duplicados
        pre: modifica el diccionario

        /*var
        diccionario es un diccionario
        termino es STR
        archivo_o_directorio es STR
        path es STR
    """
    if termino == "" :
        return

    if termino not in diccionario:
        diccionario[termino] = [ruta]
        return

    if ruta not in diccionario[termino]:
        diccionario[termino].append(ruta)
        return

def agregar_lista_invertida_archivos(diccionario, archivo, ruta):
    """Agrega al diccionario nombre de archivo y su contenido con su respectiva ruta
        pre: solo se indexara el contenido de los archivos con extencion [txt,py,c,md]

        /*var
        diccionario es un diccionario
        files es STR
        path es STR

        se modifica el contenido del diccionario
    """
    if archivo == "":
        return

    for termino in re.split("\W+", archivo):
        evita_duplicado(diccionario, termino, ruta )

    if archivo.split(".")[1] in c.ARCHIVOS: #archivos

        with open(ruta) as _file:

            for line in _file:
                for termino in re.split("\W+",line.rstrip()):
                    evita_duplicado(diccionario, termino.lower(), ruta)


#modifique los parametros de la funcion
def agregar_lista_invertida_directorios(diccionario,directorio,ruta):
    """Agrega al diccionario los directorios y su contenido con su respectiva ruta
        pre: al indexar las rutas se tendra en cuenta las subdirectorios correspondientes con sus archivos

        /*var
        diccionario es un diccionario
        directorio es STR
        ruta es STR

        se modifica el contenido del diccionario
    """
    if directorio == "":
        return

    for termino in re.split("\W+",directorio):

        if not SO.listdir(ruta):
            evita_duplicado(diccionario, termino, ruta)
            continue

        for archivo in SO.listdir(ruta):
            ruta_archivo = SO.path.join(ruta, archivo.lower())
            evita_duplicado(diccionario, termino.lower(), ruta_archivo)

    return

def recorrer_arbol_directorios():
    """Recorre el directorio actual y los subdirectorios
       post: retorna la cantidad de archivos procesados y un diccionario que es la lista_invertida
    """
    cant_archivos = 0
    lista_invertida = {}

    for path , directorios, archivos in SO.walk("."):

        for directorio in directorios:
            ruta_directorio = SO.path.join(path.lower(), directorio.lower())
            agregar_lista_invertida_directorios(lista_invertida, directorio.lower(), ruta_directorio)

        for archivo in archivos:
            ruta_archivo = ruta = SO.path.join(path.lower(), archivo.lower())
            agregar_lista_invertida_archivos(lista_invertida, archivo.lower(), ruta_archivo)
            cant_archivos += 1

    return cant_archivos, lista_invertida
