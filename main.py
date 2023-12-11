from grafo import *
from carga_datos import *
from operaciones import *
from test_grafo import *
def main():

    grafo = crear_grafo_internet("/home/lucas/Escritorio/tp3/wiki.tsv")
    # conectado= conectados(grafo, "Argentina") esto no lo pude comprobar porque se me queda sin memoria la maquina virtual
    # print(conectado)
    listar_operaciones()
        
if __name__ == "__main__":
    main()