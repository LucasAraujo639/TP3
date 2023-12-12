from grafo import *
from operaciones import *

def lectura_comandos(grafo, entrada_comandos):

    ultima_cfc_solicitada = set()

    for linea in entrada_comandos:

        # Quitar caracteres de espacio del extremo del comando.
        linea = linea.rstrip()

        # Parsear comando.
        elementos = linea.split(" ")

        # Obtención de comando y parámetros de invocación.
        comando, parametros = obtener_comando_y_parametros(elementos)

        # Ejecución de comandos.
        if comando == Comando.LISTAR_OPERACIONES:
            listar_operaciones()

        elif comando == Comando.DIAMETRO:
            imprimir_diametro(diametro(grafo))

        elif comando == Comando.CONECTIVIDAD:
            origen = obtener_parametro_conectados(parametros)

            if origen not in ultima_cfc_solicitada:
                ultima_cfc_solicitada = conectados(grafo, origen)

            imprimir_cfc(ultima_cfc_solicitada)

        elif comando == Comando.ORDEN_LECTURA:
            paginas = obtener_parametros_orden_lectura(parametros)

            imprimir_lectura(lectura(grafo, paginas))

        elif comando == Comando.NAV_PRIMER_LINK:
            origen = obtener_pagina_origen_nav(parametros)

            imprimir_camino_nav_primer_link(navegacion(grafo, origen))

        elif comando == Comando.CAMINO_MAS_CORTO:
            origen, destino = obtener_parametros_camino_mas_corto(parametros)
            
            imprimir_camino_mas_corto(camino_mas_corto(grafo, origen, destino))

        elif comando == Comando.COMUNIDADES:
            pagina = obtener_parametro_comunidad(parametros)
            imprimir_comunidad(comunidad(grafo, pagina))

        elif comando == Comando.CLUSTERING:
            pagina = obtener_pagina_coef_clustering(parametros)

            coef = 0.0

            if pagina == None:
                coef = calcular_coef_clustering_promedio(grafo)
            else:
                coef = calcular_coef_clustering_vertice(grafo, pagina)
            
            imprimir_coef_clustering(coef)
        
        elif comando == Comando.RANGO:
            origen, limite = obtener_parametros_rango(parametros)

            imprimir_paginas_rango(rango(grafo, origen, limite))

        else:
            print("Comando no válido.")


# -------------------------------------
# Funciones de obtención de parámetros.
# -------------------------------------


# Posición de elementos en comando ingresado.
POSICION_COMANDO_CMD = 0 

CANT_ELEMENTOS_COMANDO_SIN_PARAM = 1

# Obtención de comando a ejecutar.
def obtener_comando_y_parametros(elementos_entrada):
    if len(elementos_entrada) == 0:
        return Comando.ERROR, []

    if elementos_entrada[POSICION_COMANDO_CMD] not in DICCIONARIO_COMANDOS:
        return Comando.ERROR, []

    comando = DICCIONARIO_COMANDOS[elementos_entrada.pop(POSICION_COMANDO_CMD)]

    if len(elementos_entrada) == 0:
        return comando, []

    return comando, elementos_entrada

# Parámetros de comando de conectividad:
def obtener_parametro_conectados(parametros):
    return unir_elementos_con_espacio(parametros)

# Parámetros de comando de orden de lectura.
def obtener_parametros_orden_lectura(parametros):
    paginas = obtener_parametros_separados_coma(parametros)

    return paginas

# Parámetros de comando de navegación a través del primer link:
POSICION_ORIGEN_NAV_CMD = 0

def obtener_pagina_origen_nav(parametros):
    return unir_elementos_con_espacio(parametros)

# Parámetros de comando de camino más corto:
POSICION_ORIGEN_CAMINO_MAS_CORTO_CMD = 0
POSICION_DESTINO_CAMINO_MAS_CORTO_CMD = 1

def obtener_parametros_camino_mas_corto(parametros):
    parametros = obtener_parametros_separados_coma(parametros)
    return parametros[POSICION_ORIGEN_CAMINO_MAS_CORTO_CMD], parametros[POSICION_DESTINO_CAMINO_MAS_CORTO_CMD]

# Parámetros de comando de comunidades:
POSICION_PAGINA_COMUNIDAD_CMD = 0

def obtener_parametro_comunidad(parametros):
    return parametros[POSICION_PAGINA_COMUNIDAD_CMD]

# Parámetros de comando de clustering.
POSICION_PAGINA_COEF_CLUST_CMD = 0
SEPARADOR_PARAMETROS_CLUST = ' '

def obtener_pagina_coef_clustering(parametros):
    if len(parametros) > 0:
        return unir_elementos_con_espacio(parametros)
    return None

# Parámetros de comando de búsqueda de páginas a un cierto rango.
POSICION_ORIGEN_RANGO_CMD = 0
POSICION_RANGO_CMD = 1

def obtener_parametros_rango(parametros):
    parametros = obtener_parametros_separados_coma(parametros)

    limite = int(parametros[POSICION_RANGO_CMD])
    return parametros[POSICION_ORIGEN_RANGO_CMD], limite

# unir_elementos_con_espacio une las palabras pasadas por argumento con espacios.
SEPARADOR_PARAMETROS = " "

def unir_elementos_con_espacio(elementos):
    if len(elementos) == 1:
        return elementos[0]
    
    return SEPARADOR_PARAMETROS.join(elementos)

# obtener_parametros_separados_coma une los elementos con espacios y los separa por comas.
def obtener_parametros_separados_coma(parametros):
    parametros = unir_elementos_con_espacio(parametros)

    parametros = parametros.split(',')

    return parametros