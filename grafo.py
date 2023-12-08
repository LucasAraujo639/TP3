import random
from test_grafo import *


"""METODOS DEL GRAFO
# agregar_vertice(self, v)
# borrar_vertice(self, v)
# agregar_arista(self, v, w, peso = 1)
# borrar_arista(self, v, w)
# estan_unidos(self, v, w)
# peso_arista(self, v, w)
# obtener_vertices(self)
# vertice_aleatorio(self)
# adyacentes(self, v)
# str
"""
class Grafo:
    def __init__(self, es_dirigido = True):
        self.vertices = {}
        self.adyacentes = {}
        self.es_dirigido = es_dirigido
    
    def agregar_vertice(self, v):
        self.vertices[v] = v
        self.adyacentes[v] = {}
    def borrar_vertice(self, v):
        try:
            del(self.vertices[v])
            del(self.adyacentes[v])
            for w in self.adyacentes:
                if v in self.adyacentes[w]:
                    del self.adyacentes[w][v]
        except KeyError:
            print("El vertice no existe")
            
    def agregar_arista(self, v, w, peso = 1): 
        try:
            self.adyacentes[v][w] = peso
            if not self.es_dirigido:
                self.adyacentes[w][v] = peso
        except KeyError:
            print("Vertice/s no existe")
            
    def esdirigido(self):
        return self.es_dirigido
    
    def borrar_arista(self, v, w):
        try:
            if self.estan_unidos:
                del(self.adyacentes[v][w])
                if not self.es_dirigido:
                    del(self.adyacentes[w][v])
        except KeyError:
            print("La arista no existe")
                       
    def estan_unidos(self, v, w):
        return w in self.adyacentes[v]
    
    def peso_arista(self, v, w):
        try:
            if self.estan_unidos:
                return self.adyacentes[v][w]
        except KeyError:
            print("La arista no existe")
            
    def obtener_vertices(self):
        return list(self.vertices)
             
    def vertice_aleatorio(self):
        return random.choice(list(self.vertices))
    
    def adyacentes(self, v):
        return list(self.adyacencias[v])
            
    def str(self):
        return str(self.adyacentes) # Devuelve una cadena de adyacentes
    

def main():
    grafo = Grafo(es_dirigido=True)
    if test_grafo_agregar(grafo):
        print("OK")
    else:
        print("ERROR")
    
    if test_grafo_borrar(grafo):
        print("OK")
    else:
        print("ERROR")
        
if __name__ == "__main__":
    main()