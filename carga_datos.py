from grafo import *

# crear_grafo_internet carga los datos de las páginas en un grafo.
def crear_grafo_internet(direccion):
    grafo_nuevo = Grafo()
    guardados = set()

    # Lee los datos del archivo.
    with open(direccion, "rt") as archivo:
        for linea in archivo:
            linea = linea.rstrip()
            # Se separan los datos según el formato de los archivos.
            datos_parseados = linea.split("\t")

            # El primer elemento siempre es la página.
            pagina = datos_parseados.pop(0)
            grafo_nuevo.agregar_vertice(pagina)

            # Se recorre el resto de los datos ya que son los adyacentes al vértice.
            for ady in datos_parseados:

                if ady in guardados:
                    grafo_nuevo.agregar_vertice(ady)

                grafo_nuevo.agregar_arista(pagina, ady)
    
    return grafo_nuevo