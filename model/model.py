import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.DiGraph()
        self._idMap = {}

    def fillDDmetodo(self):
        return DAO.getMetodi()

    def fillDDanno(self):
        return DAO.getAnni()

    def creaGrafo(self, anno, metodo, numeroS):
        # pulisco il grafo
        self._grafo.clear()

        # creo i nodi e li aggiungo
        lista_nodi = DAO.getNodes(anno, metodo)
        for l in lista_nodi:
            self._grafo.add_node(l)
            self._idMap[l.id] = l

        # creo gli archi (grafo non orientato)
        lista_archi = DAO.getEdges(anno, metodo, numeroS)
        for a in lista_archi:
             self._grafo.add_edge(self._idMap[a[0]], self._idMap[a[1]])

    def graphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def getProdRedditizzi(self):
        lista_nodi = self._grafo.nodes
        lista_p_reddittizzi = []
        for n in lista_nodi:
            nArchiIn = self._grafo.in_degree(n)
            nArchiOut = self._grafo.out_degree(n)
            if nArchiOut == 0:
                lista_p_reddittizzi.append((n, nArchiIn))
        lista_ordinata = sorted(lista_p_reddittizzi, key=lambda x: x[1], reverse=True)
        return lista_ordinata[:5]