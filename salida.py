import sys

# imprimir_camino imprime en la salida estándar los elementos de la lista pasada por argumento con el
# formato: elemento1 -> elemento2 -> elemento3 -> ... -> elementoN
def imprimir_camino(camino):
    sys.stdout.write(camino.pop(0))

    while len(camino) > 0:
        sys.stdout.write(" -> ")
        sys.stdout.write(camino.pop(0))

    sys.stdout.write('\n')


# imprimir_conjunto imprime los elementos del conjunto pasado por argumento por la salida estándar con el
# formato: elemento1, elemento2, elemento3, ... , elementoN
def imprimir_conjunto(conjunto):
    lista = list(conjunto)
    imprimir_lista_sin_orden(lista)


# imprimir_lista_sin_orden imprime los elementos de la lista pasada por argumento por la salida estándar con el
# formato: elemento1, elemento2, elemento3, ... , elementoN
def imprimir_lista_sin_orden(lista):
    sys.stdout.write(lista.pop(0))

    while len(lista) > 0:
        sys.stdout.write(", ")
        sys.stdout.write(lista.pop(0))

    sys.stdout.write('\n')

# Diametro
# imprimir_diametro imprime el diámetro del grafo.
def imprimir_diametro(camino_diametro):
    imprimir_camino(camino_diametro)
    sys.stdout.write("Costo: ")
    sys.stdout.write(str(len(camino_diametro) - 1))
    sys.stdout.write('\n')

# Rango
# imprimir_paginas_rango imprime la cantidad de páginas encontradas.
def imprimir_paginas_rango(cantidad):
    sys.stdout.write(str(cantidad))
    sys.stdout.write('\n')

# Conectividad
# imprimir_cfc imprime la componente fuertemente conexa pasada por argumento.
def imprimir_cfc(cfc):
    if len(cfc) == 0:
        return

    imprimir_conjunto(cfc)

# Lectura (Orden topológico):
# imprimir_diametro imprime el diámetro del grafo.
def imprimir_lectura(orden_topologico):

    if len(orden_topologico) == 0:
        sys.stdout.write("No existe forma de leer las paginas en orden\n")
    else:
        imprimir_lista_sin_orden(orden_topologico)

# Navegacion por primer link:
# imprimir_camino_nav_primer_link
def imprimir_camino_nav_primer_link(camino):
    imprimir_camino(camino)

# Camino más corto:
# imprimir_camino_mas_corto
def imprimir_camino_mas_corto(camino):
    if len(camino) == 0:
        sys.stdout.write("No se encontro recorrido\n")
        return

    imprimir_camino(camino)
    sys.stdout.write("Costo: ")
    sys.stdout.write(str(len(camino) - 1))
    sys.stdout.write('\n')


# Comunidades:
# imprimir_comunidad
def imprimir_comunidad(comunidad):
    for v in comunidad:
        sys.stdout.write(v)
        sys.stdout.write('\n')
        
# Coeficiente de Clustering:    
# imprimir_coef_clustering imprime el coeficiente de clustering a tres decimales.
def imprimir_coef_clustering(coef):
    sys.stdout.write("{:.3f}".format(coef) + '\n')