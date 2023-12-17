from collections import deque
from grafo import *
from salida import *
from lectura_comandos import *
from funciones import *
from enum import Enum
import random
import sys

# Constantes
MIN_GRADO_SALIDA_COEF_CLUSTERING = 2
MAX_ITER =  20
FACTOR_ITERACIONES_COMUNIDAD = 3


# Listar operaciones:
def listar_operaciones():
    for operacion in DICCIONARIO_OPERACIONES:
        print(operacion + '\n')




# diametro devuelve el diámetro del grafo.
def diametro(grafo):
    diametro = []
    for v in grafo.obtener_vertices():
        camino_min_mas_grande = _obtener_distancias_maximas_bfs(grafo,v)

        if len(camino_min_mas_grande) > len(diametro):
            diametro = camino_min_mas_grande

    return diametro

# Rango

# Permite obtener la cantidad de páginas que se encuenten a exactamente
# n links/saltos desde la página pasada por parámetro.
def rango(grafo,vertice_origen, n):
    visitados = set()
    cola = deque()
    resultado = []
    orden = {}
    cola.append(vertice_origen)
    visitados.add(vertice_origen)
    orden[vertice_origen] = 0
    while len(cola) > 0:
        v = cola.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                orden[w] = orden[v] + 1
                visitados.add(w)
                if orden[w] == n:
                    resultado.append(w)
                elif orden[w] < n:
                    cola.append(w)
    return len(resultado)

# conectividad muestra todas las páginas a los que se puede llegar desde la página pasada por parámetro y
# que, a su vez, puedan también volver a dicha página.
def conectados(grafo, vertice_origen):
    sys.setrecursionlimit(500000)
    resultados = []
    visitados = set()
    for v in grafo.obtener_vertices():
        if v not in visitados:
            _dfs_tarjan(grafo,vertice_origen,resultados, visitados,deque(), set(), {},{},[0])
            
    for cfc in resultados:
        if vertice_origen in cfc:
            return cfc
    return []
# Lectura
# Orden topológico:
# lectura permite obtener un orden en el que es válido leer las páginas indicados.
def lectura(grafo, paginas):
    grados = _grados_salida(grafo, paginas)
    vertices= _vertices_entrada(grafo, paginas)
    cola = deque()
    for vertice in paginas:
        if grados[vertice] == 0:
            cola.append(vertice)
    lectura_orden = []
    while not len(cola) == 0:
        v = cola.popleft()
        lectura_orden.append(v)
        vertice_entrada = vertices[v]
        for w in vertice_entrada:
            if w in paginas:
                grados[w] -= 1
                if grados[w]== 0:
                    cola.append(w)

    if len(lectura_orden) != len(paginas): # No hay un ciclo
        return []
    
    return lectura_orden


# Navegacion por primer link:


# navegacion_primer_link navega usando el primer link desde la página "origen" y navega usando siempre el primer link hasta
# que no hay más links o se llegue a hayan visto 20 páginas.
def navegacion(grafo, origen):
    navegacion = [origen]
    actual = origen
    for i in range(MAX_ITER):
        if len(grafo.adyacentes(actual)) == 0:
            break
        actual = grafo.adyacentes(actual)[0]
        navegacion.append(actual)
        

    return navegacion

# camino_mas_corto busca el camino más corto de un grafo desde el elemento "origen" hasta el elemento "destino".
def camino_mas_corto(grafo, origen, destino):
    cola = deque()
    visitados = set()
    padres = {}

    cola.append(origen)
    visitados.add(origen)
    padres[origen] = None

    while len(cola) > 0:
        v = cola.popleft()

        for w in grafo.adyacentes(v):
            
            if w not in visitados:
                visitados.add(w)
                cola.append(w)
                padres[w] = v

                if w == destino:
                    return _reconstruir_camino(padres, origen, destino)

    return []


# comunidad devuelve las páginas que pertenecen a la comunidad a la que pertenece la página "pagina" pasada por parámetro.
def comunidad(grafo, pagina):
    etiquetas = {}
    orden_analisis = {}
    vertices_entrantes = {}

    cantidad_vertices = len(grafo.obtener_vertices())

    # Establece el valor de las etiquetas.
    for i, v in enumerate(grafo.obtener_vertices(), 0):
        etiquetas[v] = i
        orden_analisis[i] = v

        if v not in vertices_entrantes:
            vertices_entrantes[v] = set()

        for w in grafo.adyacentes(v):
            if w not in vertices_entrantes[v]:
                vertices_entrantes[v].add(w)

    # Aleatoriza posiciones de lectura.
    for i in range(len(grafo.obtener_vertices())):
        nueva_pos = random.randint(0, cantidad_vertices-1)
        orden_analisis[nueva_pos], orden_analisis[i] = orden_analisis[i], orden_analisis[nueva_pos]

    # Agrupa los vértices en comunidades.
    for _ in range(FACTOR_ITERACIONES_COMUNIDAD):

        for indice in range(0, cantidad_vertices):
            v = orden_analisis[indice]

            etiquetas[v] = _max_frec(etiquetas, vertices_entrantes[v])

        # Crea la lista con los elementos de la comunidad.
        etiqueta_pagina = etiquetas[pagina]
        lista_comunidad = []

    # Crear lista de comunidad de la palabra buscada.
    for v in grafo.obtener_vertices():
        if etiqueta_pagina == etiquetas[v]:
            lista_comunidad.append(v)

    return lista_comunidad





# calcular_coef_clustering_promedio calcula el coeficiente de clustering promedio del grafo.
def calcular_coef_clustering_promedio(grafo):
    suma_coefs = 0.0

    for v in grafo.obtener_vertices():
        suma_coefs += calcular_coef_clustering_vertice(grafo, v)
    
    return suma_coefs / len(grafo.obtener_vertices())


# calcular_coef_clustering_vertice calcula el coeficiente de clustering de un único vértice.
def calcular_coef_clustering_vertice(grafo, origen):

    grado_salida = len(grafo.adyacentes(origen))

    if grado_salida < MIN_GRADO_SALIDA_COEF_CLUSTERING:
        return 0.0

    cant_ady_conectados = 0

    for ady1 in grafo.adyacentes(origen):

        # Evita el bucle
        if ady1 == origen:
            continue

        for ady2 in grafo.adyacentes(origen):

            # Evita el bucle
            if ady2 == origen:
                continue

            # Evita que los vértices sean iguales.
            if ady1 == ady2:
                continue

            # Si hay una arista que une los adyacentes analizados, se suma a la cantidad.
            if grafo.estan_unidos(ady1, ady2):
                cant_ady_conectados += 1

    # Se calcula el valor del coeficiente y se devuelve el resultado.
    return cant_ady_conectados / ((grado_salida - 1)*grado_salida)