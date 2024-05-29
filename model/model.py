import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}
        sales_volume = {}

    def getCountries(self):
        return DAO.getAllCountries()

    def creaGrafo(self,country,year):
        self._idMap = {}
        self._grafo.clear()
        self.nodi = DAO.getAllretailersCountry(country)
        for n in self.nodi:
            self._idMap[n.Retailer_code] = n

        self._grafo.add_nodes_from(self.nodi)
        for n1 in self.nodi:
            for n2 in self.nodi:
                if n1 != n2:
                    count = DAO.getProductsInCommon(n1,n2,year)
                    if count[0] > 0:
                        self._grafo.add_edge(n1,n2, weight = count[0])
    def calculate_sales_volume(self):
        sales_volume= {}
        for nodo in self._grafo.nodes():
            volume = sum(data["weight"] for _,_, data in self._grafo.edges(nodo, data = True))
            sales_volume[nodo] = volume
        return sales_volume


    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)