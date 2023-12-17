from collections import deque
from grafo import *
from enum import Enum
from salida import *
from lectura_comandos import *
import random








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








# Conectividad:





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






