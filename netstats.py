from collections import deque
from grafo import *
from funciones import *
from test_grafo import *
def conectividad(grafo, vertice_origen):
    resultados = []
    visitados = set()
    for v in grafo:
        if v not in visitados:
            dfs_tarjan(grafo,vertice_origen,resultados, visitados,deque(), set(), {},{},[0])
    return resultados

       
    
#Orden topologico
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

    if len(lectura_orden) != len(paginas): # Hay un ciclo
        return print("No existe forma de leer las paginas en orden")
    
    return lectura_orden
  
    
def navegacion_primer_link(grafo, origen):
    navegacion = [origen]
    actual = origen
    for i in range(20):
        if len(grafo.adyacentes(actual)) > 0:
            break
        actual = grafo.adyacentes(actual)[0]
        navegacion.append(actual)
        

    return navegacion

    