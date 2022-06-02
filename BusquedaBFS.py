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
	
    def agregar_arista(self, nodo1, nodo2, peso=1):
        """
        Agrega un arista al Grafo

        Si el argumento peso no es pasado,  toma como valor por defecto 1

        Parametros
        ----------
        nodo1 : entero
            Número de nodo1
        nodo2 : entero
            Número de nodo2
        peso : entero (opcional)
            Peso del arista. por defecto 1.

        Retorna
        -------
        None
        """

        # Agregar nodo2 a lista en nodo1
        self.m_lista_adyacencia[nodo1].add((nodo2, peso))
        # No Dirigido?
        if not self.m_dirigido:
            # Agregar nodo 1 a lista en nodo2
            self.m_lista_adyacencia[nodo2].add((nodo1, peso))
    
    def imprimir_lista_adyacente(self):
        """
        Imprime la lista de adyacencia

        Parametros
        ----------
        Ninguno

        Retorna
        -------
        nodo$(llave): {m_lista_adyacencia[llave]}
        """

        #Recorre por la lista de adyacencia
        for llave in self.m_lista_adyacencia.keys():
            # Imprimir nodo con la lista de adyacencia
            print("nodo", llave, ": ", self.m_lista_adyacencia[llave])

    def bfs_transversal(self, nodo_inicial):
        """
        Imprime el recorrido BFS (Búsqueda en anchura) de un vértice fuente dado y atraviesa vértices alcanzables desde s.

        Parametros
        ----------
        nodo_inicial : entero
            Nodo inicial del Grafo a imprimir

        Retorna
        -------
        Recorrido de nodos ( 0 1 2 4 3 ...)
        """
        # Conjunto de nodos visitados para evitar bucles
        visitado = set()
        cola = Queue()
        # agrega nodo_inicial a la cola
        cola.put(nodo_inicial)
        # agrega a la lista visitada
        visitado.add(nodo_inicial)

        # Bucle de impresion de nodos
        while not cola.empty():
            # Quitar un vértice de la cola
            nodo_actual = cola.get()
            # Imprime el vertice
            print(nodo_actual, end = " ")

            # Obtener todos los vértices adyacentes del vértice eliminado. 
            for (siguiente_nodo, peso) in self.m_lista_adyacencia[nodo_actual]:
                # el nodo no ha sido visitado?
                if siguiente_nodo not in visitado:
                    #ponerlo en cola
                    cola.put(siguiente_nodo)
                    #marcarlo como visitado
                    visitado.add(siguiente_nodo)

#Verificacion de script ejecutado como principal
if __name__ == "__main__":
    # Crear un Ejemplo con una instancia de la clase `Grafo` con 5 nodos y no dirigido
    g = Grafo(5, dirigido=False)
    #agrega la arista al grafo con peso predeterminado = 1
    g.agregar_arista(2, 4)
    #agrega la arista al grafo con peso predeterminado = 1
    g.agregar_arista(1, 0)
    #agrega la arista al grafo con peso predeterminado = 1
    g.agregar_arista(3, 4)
    #agrega la arista al grafo con peso predeterminado = 1
    g.agregar_arista(1, 3)
    #agrega la arista al grafo con peso predeterminado = 1
    g.agregar_arista(2, 3)

    # Imprime la lista de adyacencia en el formulario nodo n: {(nodo, peso)}
    g.imprimir_lista_adyacente()
    # Imprime un mansaje con la acción ejecutada
    print ("A continuación se muestra el recorrido primero en anchura"
                    " (a partir del vértice 0)")
    # Imprime el recorrido
    g.bfs_transversal(0)
    # Imprime salto
    print()

    #Crear un Ejemplo con una instancia de la clase `Grafo` con 6 nodos y no dirigido
    g = Grafo(6, dirigido=False)
    #agrega la arista al grafo con peso predeterminado = 2
    g.agregar_arista(5, 0, 2)
    #agrega la arista al grafo con peso predeterminado = 3
    g.agregar_arista(2, 5, 3)
    #agrega la arista al grafo con peso predeterminado = 4
    g.agregar_arista(3, 4, 4)
    #agrega la arista al grafo con peso predeterminado = 3
    g.agregar_arista(1, 2, 3)
    #agrega la arista al grafo con peso predeterminado = 2
    g.agregar_arista(4, 5, 2)
    #agrega la arista al grafo con peso predeterminado = 2
    g.agregar_arista(2, 3, 2)

    # Imprime la lista de adyacencia en el formulario nodo n: {(nodo, peso)}
    g.imprimir_lista_adyacente()
    # Imprime un mansaje con la acción ejecutada
    print ("A continuación se muestra el recorrido primero en anchura"
                    " (a partir del vértice 0)")
    # Imprime el recorrido
    g.bfs_transversal(0)
    # Imprime salto
    print()

    #Crear un Ejemplo con una instancia de la clase `Grafo` con 7 nodos y no dirigido
    g = Grafo(7, dirigido=False)
    #agrega la arista al grafo con peso predeterminado = 1
    g.agregar_arista(1, 3)
    #agrega la arista al grafo con peso predeterminado = 1
    g.agregar_arista(2, 4)
    #agrega la arista al grafo con peso predeterminado = 1
    g.agregar_arista(4, 5)
    #agrega la arista al grafo con peso predeterminado = 1
    g.agregar_arista(6, 0)
    #agrega la arista al grafo con peso predeterminado = 1
    g.agregar_arista(3, 6)
    #agrega la arista al grafo con peso predeterminado = 1
    g.agregar_arista(2, 5)
    #agrega la arista al grafo con peso predeterminado = 1
    g.agregar_arista(6, 2)

    # Imprime la lista de adyacencia en el formulario nodo n: {(nodo, peso)}
    g.imprimir_lista_adyacente()
    # Imprime un mansaje con la acción ejecutada
    print ("A continuación se muestra el recorrido primero en anchura"
                    " (a partir del vértice 0)")
    # Imprime el recorrido
    g.bfs_transversal(0)
    # Imprime salto
    print()