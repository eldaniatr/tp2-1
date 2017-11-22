def calcular_diferencia(conjunto_A,conjunto_B):
    """Dados dos conjuntos devuelve un nuevo conjunto(lista nueva) de los elementos conjunto A que no estan en el conjunto B
        conjunto_A = lista
        conjunto_B = lista (#lista negacion)
     """
    nuevo_conjunto = []

    for elemento_A in conjunto_A:
        if elemento_A not in conjunto_B: #not lista
            nuevo_conjunto.append(elemento_A)

    return nuevo_conjunto

def calcular_interseccion(diccionario,lista_terminos):
    """ calcula la interseccion de conjuntos retornando una lista con elementos q se encuentran en todos los conjuntos a la misma vez
        lista_terminos = lista
        nuevo_conjunto = lista
    """
    k0,k1 = lista_terminos[0], lista_terminos[1]

    nuevo_conjunto = _intersecar_conjuntos(diccionario[k0],diccionario[k1])

    if not nuevo_conjunto or len(lista_terminos) == 2:
        return nuevo_conjunto

    for i in range(2, len(lista_terminos)):
        k = lista_terminos[i]
        nuevo_conjunto = _intersecar_conjuntos(nuevo_conjunto,diccionario[k])

        if not nuevo_conjunto:
            return nuevo_conjunto

    return nuevo_conjunto



def _intersecar_conjuntos(conjunto_A, conjunto_B):
    """ Inteseca dos conjuntos devolviendo un nuevo conjunto (lista) con los elementos que se encuentrar en los 2 conjuntos"""
    nuevo_conjunto = []

    for elemento_A in conjunto_A:
        if elemento_A in conjunto_B:
            nuevo_conjunto.append(elemento_A)

    return nuevo_conjunto

def verifica_terminos(diccionario, terminos):
    """Verifica los terminos para el caso and retornando True en caso que todos los terminos estan en el diccionario o False en caso contrario
        terminos = lista
     """
    ok = True
    saltar_primero = True

    for k in terminos:
        if saltar_primero:
            saltar_primero = False
            continue

        if diccionario.get(k.lower(),[]) == []:
            ok = False
            return ok
    return ok

def cargar_terminos(terminos):
    """ Carga los terminos en una lista para el caso AND retornando una lista nueva """
    lista_terminos = []
    saltar_primero = True

    for k in terminos:
        if saltar_primero:
            saltar_primero = False
            continue

        lista_terminos.append(k.lower())

    return lista_terminos



def agregar_rutas(lista,rutas):
    """ Agrega las rutas a la lista evitando su duplicado
        modifica la lista original
    """
    for ruta in rutas:
        if ruta not in lista:
            lista.append(ruta)
