# Importar libreria queue
from queue import Queue

# Declarar clase Grafo
class Grafo:
    """
    Clase para representar un grafo

    ...

    Atributos
    ----------
    m_num_de_nodos : entero
        numero de nodos de grafo
    m_nodos : range
        rango de nodos
    m_dirigido : booleano
        Estado de dirigido
    m_lista_adyacencia : Colección de tipo diccionario
        Lista de ayacencia

    Metodos
    -------
    agregar_arista(nodo1, nodo2, peso=1):
         Agregar arista al grafo.
    
    imprimir_lista_adyacente():
        Imprimir la representación del grafo

    bfs_transversal(nodo_inicial):
         Imprimir el recorrido BFS de un vértice fuente dado.
    
    """
    #Se establece el constructor con los atributos
    def __init__(self, num_de_nodos, dirigido=True):
        """
        Construye todo los atributos necesarios para el objeto Grafo.

        Parametros
        ----------
            num_de_nodos : entero
                Numero de nodos de grafo
            dirigido : booleano
                Estado de dirigido
        """
        #atributos sef.m_num_de_nodos será igual al número de nodos
        self.m_num_de_nodos = num_de_nodos
        #Rango con numero de nodos
        self.m_nodos = range(self.m_num_de_nodos) 
        #Dirigino o no dirigido
        self.m_dirigido = dirigido
        # Usamos un diccionario para implementar una lista de adyacencia      
        self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos}
	
  
    
   
    print()