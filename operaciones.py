from collections import deque
from grafo import *
from test_grafo import *

import random

# Operaciones:

# Diámetro de un grafo:

# diametro devuelve el diámetro del grafo.
def diametro(grafo):
    diametro = 0
    for v in grafo:
        dist_max = _obtener_distancias_radiales_bfs(grafo,v)

        if dist_max > diametro:
            diametro = dist_max

    return diametro

# _obtener_distancias_radiales_bfs devuelve la distancia mínima más grande de un vértice a todos los demás.
def _obtener_distancias_radiales_bfs(grafo, v):
    cola = deque()
    visitados = set()
    distancias = {}

    cola.append(v)
    visitados.add(v)
    distancias[v] = 0

    dist_max = 0

    while len(cola) > 0:
        v = cola.popleft()

        for w in grafo.adyacentes(v):

            if w not in visitados:
                visitados.add(w)
                cola.append(w)

                distancias[w] = distancias[v] + 1

                if dist_max < distancias[w]:
                    dist_max = distancias[w]

    return dist_max


# Conectividad:

# conectividad muestra todas las páginas a los que se puede llegar desde la página pasada por parámetro y
# que, a su vez, puedan también volver a dicha página.
def conectados(grafo, vertice_origen):
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
    mb[v] = orden[v] = contador_global[0]
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
            w = pila.popleft()
            apilados.remove(w)
            nueva_cfc.append(w)
            if w == v:
                break
        resultados.append(nueva_cfc)


# Orden topológico:

# lectura permite obtener un orden en el que es válido leer las páginas indicados.
def lectura(grafo, paginas):
    grados = calcular_grados_entrada(grafo, paginas)
    cola = deque()
    for vertice in paginas:
        if grados[vertice] == 0:
            cola.append(vertice)
    lectura_orden = []
    while not len(cola) == 0:
        v = cola.popleft()
        lectura_orden.append(v)
        for w in grafo.adyacentes(v):
            grados[w] -= 1
            if grados[w]== 0:
                cola.append(w)

    if len(lectura_orden) != len(paginas): # No hay un ciclo
        return print("No existe forma de leer las paginas en orden")
    
    return lectura_orden

# calcular_grados_entrada
def calcular_grados_entrada(grafo, paginas=None):
    grados_entrada = {}
    if paginas is None:
        for v in grafo:
            grados_entrada[v] = 0
        for v in grafo:
            for w in grafo.adyacentes(v):
                grados_entrada[w] += 1
    else:
        for v in paginas:
            grados_entrada[v] = 0
        for v in paginas:
            for w in grafo.adyacentes(v):
                grados_entrada[w] += 1
    return grados_entrada


# Navegacion por primer link:

# navegacion_primer_link navega usando el primer link desde la página "origen" y navega usando siempre el primer link hasta
# que no hay más links o se llegue a hayan visto 20 páginas.
def navegacion_primer_link(grafo, origen):
    navegacion = [origen]
    actual = origen
    for i in range(20):
        if len(grafo.adyacentes(actual)) > 0:
            break
        actual = grafo.adyacentes(actual)[0]
        navegacion.append(actual)
        

    return navegacion


# Camino más corto:

FACTOR_ITERACIONES_COMUNIDAD = 3

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

    return camino.reverse()


# Comunidades:

# comunidad devuelve las páginas que pertenecen a la comunidad a la que pertenece la página "pagina" pasada por parámetro.
def comunidad(grafo, pagina):
    etiquetas = {}
    orden_analisis = {}
    vertices_entrada = {}

    cantidad_vertices = 0

    # Establece el valor de las etiquetas.
    for cantidad_vertices, v in enumerate(grafo, 0):
        etiquetas[v] = cantidad_vertices
        orden_analisis[cantidad_vertices] = v

        if v not in vertices_entrada:
            vertices_entrada[v] = set()

        for w in grafo.adyacentes(v):
            if w not in vertices_entrada[v]:
                vertices_entrada[v].set(w)

    # Aleatoriza posiciones de lectura.
    for i in range(cantidad_vertices):
        nueva_pos = random.randint(0, cantidad_vertices)
        orden_analisis[nueva_pos], orden_analisis[i] = orden_analisis[i], orden_analisis[cantidad_vertices]

    # Agrupa los vértices en comunidades.
    for indice in range(0, FACTOR_ITERACIONES_COMUNIDAD*cantidad_vertices):
        v = orden_analisis[indice]

        etiquetas[v] = _max_frec(v, etiquetas, vertices_entrada[v])

    # Crea la lista con los elementos de la comunidad.
    etiqueta_pagina = etiquetas[pagina]
    lista_comunidad = []
    
    for v in grafo:
        if etiqueta_pagina == etiquetas[v]:
            lista_comunidad.append(v)

    return lista_comunidad

# _max_frec busca la etiqueta con más frecuencia
def _max_frec(vertice, etiquetas, vertices_entrada):
    frecuencias = {}

    # Arma un diccionario de cantidad de apariciones de las etiquetas.
    for v in vertices_entrada:
        if v not in frecuencias:
            frecuencias[etiquetas[v]] = 0
        else:
            frecuencias[etiquetas[v]] += 1
    
    # Busca la frecuencia más alta.
    max_frec_label = 0
    max_cant = 0
    for label, cant in frecuencias:
        if cant > max_cant:
            max_frec_label = label

    return max_frec_label


# Coeficiente de Clustering:

MIN_GRADO_SALIDA_COEF_CLUSTERING = 2

# obtener_coefs_clustering calcula los coeficientes de clustering de todos los vértices del grafo.
def obtener_coefs_clustering(grafo):
    coeficientes = {}

    # Itera los vértices del grafo.
    for v in grafo:
        grado_salida = len(grafo.adyacentes(v))

        if grado_salida < MIN_GRADO_SALIDA_COEF_CLUSTERING:
            coeficientes[v] = 0
            continue

        cant_ady_conectados = 0

        for ady1 in grafo.adyacentes(v):

            # Evita el bucle
            if ady1 == v:
                continue

            for ady2 in grafo.adyacentes(v):

                # Evita el bucle
                if ady2 == v:
                    continue

                # Evita que los vértices sean iguales.
                if ady1 == ady2:
                    continue

                # Si hay una arista que une los adyacentes analizados, se suma a la cantidad.
                if grafo.estan_unidos(ady1, ady2):
                    cant_ady_conectados += 1

        # Se calcula el valor del coeficiente y se guarda en el diccionario.
        coeficientes[v] = cant_ady_conectados / ((grado_salida - 1)*grado_salida)

    return coeficientes