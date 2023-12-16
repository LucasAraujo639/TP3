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