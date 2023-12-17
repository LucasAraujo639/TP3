# imprimir_camino imprime en la salida estándar los elementos de la lista pasada por argumento con el
# formato: elemento1 -> elemento2 -> elemento3 -> ... -> elementoN
def imprimir_camino(camino):
    print(camino.pop(0))

    while len(camino) > 0:
        print(" -> ")
        print(camino.pop(0))

    print('\n')


# imprimir_conjunto imprime los elementos del conjunto pasado por argumento por la salida estándar con el
# formato: elemento1, elemento2, elemento3, ... , elementoN
def imprimir_conjunto(conjunto):
    lista = list(conjunto)
    imprimir_lista_sin_orden(lista)


# imprimir_lista_sin_orden imprime los elementos de la lista pasada por argumento por la salida estándar con el
# formato: elemento1, elemento2, elemento3, ... , elementoN
def imprimir_lista_sin_orden(lista):
    print(lista.pop(0))

    while len(lista) > 0:
        print(", ")
        print(lista.pop(0))

    print('\n')


# Diametro
# imprimir_diametro imprime el diámetro del grafo.
def imprimir_diametro(camino_diametro):
    imprimir_camino(camino_diametro)
    print("Costo: ")
    print(str(len(camino_diametro) - 1))
    print('\n')

# Conectividad
# imprimir_cfc imprime la componente fuertemente conexa pasada por argumento.
def imprimir_cfc(cfc):
    if len(cfc) == 0:
        return

    imprimir_conjunto(cfc)

# Rango
# _imprimir_paginas_rango imprime la cantidad de páginas encontradas.
def imprimir_paginas_rango(cantidad):
    print(str(cantidad))
    print('\n')

# Lectura
# imprimir_diametro imprime el diámetro del grafo.
def imprimir_lectura(orden_topologico):

    if len(orden_topologico) == 0:
        print("No existe forma de leer las paginas en orden\n")
    else:
        imprimir_lista_sin_orden(orden_topologico)

# Navegacion
# imprimir_camino_nav_primer_link
def imprimir_camino_nav_primer_link(camino):
    imprimir_camino(camino)

# Camino mas corto
# imprimir_camino_mas_corto
def imprimir_camino_mas_corto(camino):
    if len(camino) == 0:
        print("No se encontro recorrido\n")
        return

    imprimir_camino(camino)
    print("Costo: ")
    print(str(len(camino) - 1))
    print('\n')


# Comunidades:
# imprimir_comunidad
def imprimir_comunidad(comunidad):
    for v in comunidad:
        print(v)
        print('\n')

# Coeficiente de Clustering:
# imprimir_coef_clustering imprime el coeficiente de clustering a tres decimales.
def imprimir_coef_clustering(coef):
    print("{:.3f}".format(coef) + '\n')