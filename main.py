from grafo import *
from carga_datos import *
from operaciones import *
from test_grafo import *
def main():
    # grafo = Grafo(es_dirigido=True)
    # if test_grafo_agregar(grafo):
    #     print("OK")
    # else:
    #     print("ERROR")
    
    # if test_grafo_borrar(grafo):
    #     print("OK")
    # else:
    #     print("ERROR")
    # print(grafo.peso_arista("C","A"))
   grafo = crear_grafo_internet("/home/lucas/Escritorio/tp3/wiki.tsv")
   l= conectados(grafo, "Argentina")
   print(l)
   
        
if __name__ == "__main__":
    main()