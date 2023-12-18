#!/usr/bin/python3

from grafo import *
from carga_datos import *
from lectura_comandos import lectura_comandos

import sys

def main():
    # Obtener archivo de lectura de datos.
    archivo = obtener_archivo_entrada_datos(sys.argv)

    # Crear grafo a utilizar.
    grafo = crear_grafo_internet(archivo)

    # Leer los comandos.
    lectura_comandos(grafo, sys.stdin)

        
if __name__ == "__main__":
    main()