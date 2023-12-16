from collections import deque
from grafo import *
from enum import Enum
from salida import *

import sys
import random

# Diccionario de operaciones:

# Comandos de entrada.
LISTAR_OPERACIONES_CMD = "listar_operaciones"
DIAMETRO_CMD = "diametro"
CONECTIVIDAD_CMD = "conectados"
ORDEN_LECTURA_CMD = "lectura"
NAV_PRIMER_LINK_CMD = "navegacion"
CAMINO_MAS_CORTO_CMD = "camino"
COMUNIDADES_CMD = "comunidad"
CLUSTERING_CMD = "clustering"
RANGO_CMD = "rango"

# Comandos para uso interno.
class Comando(Enum):
    ERROR = 0
    LISTAR_OPERACIONES = 1
    DIAMETRO = 2
    CONECTIVIDAD = 3
    ORDEN_LECTURA = 4
    NAV_PRIMER_LINK = 5
    CAMINO_MAS_CORTO = 6
    COMUNIDADES = 7
    CLUSTERING = 8
    RANGO = 9

# Diccionario para convertir comandos en formato de cadena de caracteres en una forma para uso interno.
DICCIONARIO_COMANDOS = {
    LISTAR_OPERACIONES_CMD: Comando.LISTAR_OPERACIONES,
    DIAMETRO_CMD: Comando.DIAMETRO,
    CONECTIVIDAD_CMD: Comando.CONECTIVIDAD,
    ORDEN_LECTURA_CMD: Comando.ORDEN_LECTURA,
    NAV_PRIMER_LINK_CMD: Comando.NAV_PRIMER_LINK,
    CAMINO_MAS_CORTO_CMD: Comando.CAMINO_MAS_CORTO,
    COMUNIDADES_CMD: Comando.COMUNIDADES,
    CLUSTERING_CMD: Comando.CLUSTERING,
    RANGO_CMD: Comando.RANGO
}

# Operaciones:

DICCIONARIO_OPERACIONES = {
DIAMETRO_CMD,
CONECTIVIDAD_CMD,
ORDEN_LECTURA_CMD,
NAV_PRIMER_LINK_CMD,
CAMINO_MAS_CORTO_CMD,
COMUNIDADES_CMD,
CLUSTERING_CMD,
RANGO_CMD
}

# Listar operaciones:
def listar_operaciones():
    for operacion in DICCIONARIO_OPERACIONES:
        sys.stdout.write(operacion + '\n')


# Diámetro de un grafo:

# imprimir_diametro imprime el diámetro del grafo.
def imprimir_diametro(camino_diametro):
    imprimir_camino(camino_diametro)
    sys.stdout.write("Costo: ")
    sys.stdout.write(str(len(camino_diametro) - 1))
    sys.stdout.write('\n')

# diametro devuelve el diámetro del grafo.
def diametro(grafo):
    diametro = []
    for v in grafo.obtener_vertices():
        camino_min_mas_grande = _obtener_distancias_maximas_bfs(grafo,v)

        if len(camino_min_mas_grande) > len(diametro):
            diametro = camino_min_mas_grande

    return diametro

# _obtener_distancias_maximas_bfs devuelve la distancia mínima más grande de un vértice a todos los demás.
def _obtener_distancias_maximas_bfs(grafo, origen):
    cola = deque()
    visitados = set()
    distancias = {}
    padres = {}

    cola.append(origen)
    visitados.add(origen)
    distancias[origen] = 0
    padres[origen] = None

    v_dist_max = origen

    while len(cola) > 0:
        v = cola.popleft()

        for w in grafo.adyacentes(v):

            if w not in visitados:
                visitados.add(w)
                cola.append(w)
                padres[w] = v
                distancias[w] = distancias[v] + 1

                if distancias[v_dist_max] < distancias[w]:
                    v_dist_max = w

    return _reconstruir_camino(padres, origen, v_dist_max)

# Rango

# imprimir_paginas_rango imprime la cantidad de páginas encontradas.
def imprimir_paginas_rango(cantidad):
    sys.stdout.write(str(cantidad))
    sys.stdout.write('\n')

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


# Conectividad:

# imprimir_cfc imprime la componente fuertemente conexa pasada por argumento.
def imprimir_cfc(cfc):
    if len(cfc) == 0:
        return

    imprimir_conjunto(cfc)

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

# _dfs_tarjan
def _dfs_tarjan(grafo,v,resultados, visitados, pila, apilados, mb, orden, contador_global):
    mb[v] = contador_global[0]
    orden[v] = contador_global[0]
    visitados.add(v)
    pila.append(v)
    apilados.add(v)
    contador_global[0] += 1
    for w in grafo.adyacentes(v):
        if w not in visitados:
            _dfs_tarjan(grafo,w,resultados, visitados, pila, apilados, mb, orden, contador_global)
        if w in apilados:
            mb[v] = min(mb[v], mb[w])

    if mb[v] == orden[v]:
        nueva_cfc = []
        while True:
            w = pila.pop()
            apilados.remove(w)
            nueva_cfc.append(w)
            if w == v:
                break
        resultados.append(nueva_cfc)


# Orden topológico:

# imprimir_diametro imprime el diámetro del grafo.
def imprimir_lectura(orden_topologico):

    if len(orden_topologico) == 0:
        sys.stdout.write("No existe forma de leer las paginas en orden\n")
    else:
        imprimir_lista_sin_orden(orden_topologico)

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
#_vertices_entrada
# calcula los vertices de entrada para cada vertice en un grafo o vertices seleccionados
def _vertices_entrada(grafo, paginas = None):
    vertices_entrada = {}
    if paginas is None:
        for v in grafo.obtener_vertices():
            for w in grafo.adyacentes(v):
                vertices_entrada[w] = v
    else:
        for v in paginas:
            vertices_entrada[v] = set()
        for v in paginas:
            for w in grafo.adyacentes(v):
                if not vertices_entrada or w in vertices_entrada:
                    vertices_entrada[w].add(v)
    return vertices_entrada

# _grados_salida
# Calcula los grados de salida de un grafo o de una cantidad seleccionada de vertices
def _grados_salida(grafo, paginas=None):
    grados_salida = {}
    if paginas is None:
        for v in grafo.obtener_vertices():
            grados_salida[v] = len(grafo.adyacentes(v))
        
    else:
        for v in paginas:
            grados_salida[v] = 0
        for v in paginas:
            for w in grafo.adyacentes(v):
                if w in grados_salida:
                    grados_salida[v]+=1
    return grados_salida


# Navegacion por primer link:

MAX_ITER =  20

# imprimir_camino_nav_primer_link
def imprimir_camino_nav_primer_link(camino):
    imprimir_camino(camino)

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




# Camino más corto:

FACTOR_ITERACIONES_COMUNIDAD = 3

# imprimir_camino_mas_corto
def imprimir_camino_mas_corto(camino):
    if len(camino) == 0:
        sys.stdout.write("No se encontro recorrido\n")
        return

    imprimir_camino(camino)
    sys.stdout.write("Costo: ")
    sys.stdout.write(str(len(camino) - 1))
    sys.stdout.write('\n')

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

# _reconstruir_camino devuelve el camino más corto entre "origen" y "destino".
def _reconstruir_camino(padres, origen, destino):
    camino = []
    actual = destino

    while origen != actual:
        camino.append(actual)
        actual = padres[actual]

    camino.append(origen)

    camino.reverse()

    return camino


# Comunidades:

# imprimir_comunidad
def imprimir_comunidad(comunidad):
    for v in comunidad:
        sys.stdout.write(v)
        sys.stdout.write('\n')

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

# _max_frec busca la etiqueta con más frecuencia
def _max_frec(etiquetas, vertices_entrantes):
    frecuencias = {}

    # Arma un diccionario de cantidad de apariciones de las etiquetas.
    for v in vertices_entrantes:
        if v not in frecuencias:
            frecuencias[etiquetas[v]] = 0
        else:
            frecuencias[etiquetas[v]] += 1
    
    # Busca la frecuencia más alta.
    max_frec_label = 0
    max_cant = 0
    for label in frecuencias:
        cant = frecuencias[label]
        if cant > max_cant:
            max_frec_label = label

    return max_frec_label


# Coeficiente de Clustering:

MIN_GRADO_SALIDA_COEF_CLUSTERING = 2

# imprimir_coef_clustering imprime el coeficiente de clustering a tres decimales.
def imprimir_coef_clustering(coef):
    sys.stdout.write("{:.3f}".format(coef) + '\n')

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