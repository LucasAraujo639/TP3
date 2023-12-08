from collections import deque
from grafo import *

def bfs_en_rango(grafo,vertice_origen, n):
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
                if orden[w] == 2:
                    resultado.append(w)
                elif orden[w] < 2:
                    cola.append(w)
    return resultado


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


def dfs_tarjan(grafo,v,resultados, visitados, pila, apilados, mb, orden, contador_global):
    mb[v] = orden[v] = contador_global[v]
    pila.append(v)
    apilados.add(v)
    contador_global[0] += 1
    for w in grafo.adyacentes(v):
        if w not in visitados:
            dfs_tarjan(grafo,w,resultados, visitados, pila, apilados, mb, orden, contador_global)
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