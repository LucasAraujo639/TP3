def test_grafo_agregar(g):
    respuesta_ady = {"A":{"B":3, "C":5,"D":1},"B":{"A":2},"C":{"A":22,"B":33}, "D":{}}
    respuesta_vertices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D'}
    
    g.agregar_vertice("A")
    g.agregar_vertice("B")
    g.agregar_vertice("C")
    g.agregar_vertice("D")
    g.agregar_arista("A","B",3)
    g.agregar_arista("A","C",5)
    g.agregar_arista("A","D")
    g.agregar_arista("B","A",2)
    g.agregar_arista("C","A",22)
    g.agregar_arista("C","B",33)
    
    print(g.obtener_vertices())
    print(g.adyacentes("C"))
    
    if g.obtener_vertices() != respuesta_vertices:
        return False
    if g.adyacentes != respuesta_ady:
        return False
    return True

def test_grafo_borrar(g):
    
    respuesta_ady = {"A":{"D":1},"C":{"A":22}, "D":{}}
    respuesta_vertices = {'A': 'A', 'C': 'C', 'D': 'D'}
    
    g.agregar_vertice("A")
    g.agregar_vertice("B")
    g.agregar_vertice("C")
    g.agregar_vertice("D")
    g.agregar_arista("A","B",3)
    g.agregar_arista("A","C",5)
    g.agregar_arista("A","D")
    g.agregar_arista("B","A",2)
    g.agregar_arista("C","A",22)
    g.agregar_arista("C","B",33)
    
    # Tengo esto, ahora empiezo a borrar
    # {"A":{"B":3, "C":5,"D":1},"B":{"A":2},"C":{"A":22,"B":33}, "D":{}}
    g.borrar_arista("A","C")
    g.borrar_arista("D","A") # La arista no existe
    g.borrar_arista("C","B")
    g.borrar_vertice("B")

    print(g.obtener_vertices())
    print(g.adyacentes("C"))
    
    if g.obtener_vertices() != respuesta_vertices:
        return False
    if g.adyacentes != respuesta_ady:
        return False
    return True
    
    