import random



# MÉTODOS DEL GRAFO:

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

class Grafo:
    def __init__(self, es_dirigido = True):
        self.vertices = {}
        self.es_dirigido = es_dirigido
    
    def agregar_vertice(self, v):
        self.vertices[v] = {}

    def borrar_vertice(self, v):
        try:
            del(self.vertices[v])
            if not self.es_dirigido:
                for w in self.vertices:
                    del self.vertices[w]
        except KeyError:
            print("El vertice no existe")
            
    def agregar_arista(self, v, w, peso = 1): 
        try:
            self.vertices[v][w] = peso
            if not self.es_dirigido:
                self.vertices[w][v] = peso
        except KeyError:
            print("Vertice/s no existe")
            
    def esdirigido(self):
        return self.es_dirigido
    
    def borrar_arista(self, v, w):
        try:
            if self.estan_unidos:
                del(self.vertices[v][w])
                if not self.es_dirigido:
                    del(self.adyacentes[w][v])
        except KeyError:
            print("La arista no existe")
                       
    def estan_unidos(self, v, w):
        return v in self.vertices and w in self.vertices and self.vertices[v].get(w) is not None
    
    def peso_arista(self, v, w):
        try:
            if self.estan_unidos:
                return self.vertices[v][w]
        except KeyError:
            print("La arista no existe")
            
    def obtener_vertices(self):
        lista_vertices = []
        for v in self.vertices:
            lista_vertices.append(v)
        return lista_vertices

             
    def vertice_aleatorio(self):
        return random.choice(list(self.vertices))
    
    def adyacentes(self, v):
        lista_adyacentes = []
        for w in self.vertices[v].keys():
            lista_adyacentes.append(w)
        return lista_adyacentes
            
    def str(self):
        return str(self.adyacentes) # Devuelve una cadena de adyacentes
    

