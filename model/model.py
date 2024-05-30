import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}
        sales_volume = {}
        self.ottimo = []
        self.pesoMax = 0

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

    def getPercorsoPesoMax(self,N):
        self.ottimo = []
        self.pesoMax = 0
        parziale = []
        for nodo in self.nodi:
            parziale = [nodo]
            self.ricorsione(parziale,N)
        return self.ottimo, self.pesoMax



    def ricorsione(self,parziale, N): # N è il numero di archi inseriti dall'utente minimo 2
        # condizione terminale è che parziale sia di lunghezza N , e che il primo nodo coincida con l'ultimo
        if len(parziale) > N:
            return
        if len(parziale) == N and parziale[0] == parziale[-1]:
            if len(parziale[1:-1]) == len(set(parziale[1:-1])):
                if self.calcolaPeso(parziale) > self.pesoMax:
                    self.ottimo = copy.deepcopy(parziale)
                    self.pesoMax = self.calcolaPeso(self.ottimo)
                    return

        # vertici intermedi non devono essere ripetuti
        for v in self._grafo.neighbors(parziale[-1]):
                parziale.append(v)
                self.ricorsione(parziale,N)
                parziale.pop()
            #La somma dei pesi degli archi percorsi deve essere massima.

    def calcolaPeso(self,lista):
        peso = 0
        for i in range(len(lista)-1):
            peso += self._grafo[lista[i]][lista[i+1]]["weight"]
        return peso