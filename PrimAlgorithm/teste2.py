
graph_lista = {
    "v1": {"v1": 0, "v2": 1, "v3": 0, "v4": 0, "v5": 6, "v6": 5, "v7": 0, "v8": 0, "v9": 5},
    "v2": {"v1": 1, "v2": 0, "v3": 2, "v4": 0, "v5": 3, "v6": 0, "v7": 0, "v8": 5, "v9": 3},
    "v3": {"v1": 0, "v2": 2, "v3": 0, "v4": 5, "v5": 4, "v6": 9, "v7": 0, "v8": 0, "v9": 0},
    "v4": {"v1": 0, "v2": 0, "v3": 5, "v4": 0, "v5": 2, "v6": 6, "v7": 3, "v8": 0, "v9": 0},
    "v5": {"v1": 6, "v2": 3, "v3": 4, "v4": 2, "v5": 0, "v6": 1, "v7": 8, "v8": 4, "v9": 1},
    "v6": {"v1": 0, "v2": 0, "v3": 9, "v4": 6, "v5": 1, "v6": 0, "v7": 4, "v8": 0, "v9": 0},
    "v7": {"v1": 0, "v2": 0, "v3": 0, "v4": 3, "v5": 8, "v6": 4, "v7": 0, "v8": 2, "v9": 0},
    "v8": {"v1": 0, "v2": 5, "v3": 0, "v4": 0, "v5": 4, "v6": 0, "v7": 2, "v8": 0, "v9": 4},
    "v9": {"v1": 5, "v2": 3, "v3": 0, "v4": 0, "v5": 1, "v6": 0, "v7": 0, "v8": 4, "v9": 0}
}
graph_dict = {"v1": {"v1": 0, "v2": 2, "v3": 3, "v4": 0, "v5": 3},
              "v2": {"v1": 1, "v2": 0, "v3": 0, "v4": 2, "v5": 3},
              "v3": {"v1": 2, "v2": 0, "v3": 0, "v4": 3, "v5": 4},
              "v4": {"v1": 3, "v2": 5, "v3": 2, "v4": 0, "v5": 0},
              "v5": {"v1": 3, "v2": 5, "v3": 2, "v4": 4, "v5": 0},
              }

def filterAdjacencia(adjacencia):
    return {k: v for k, v in adjacencia.items() if v != 0}

def getMenorArestaVertice(adjacencia,visitados):
    adjacencia = filterAdjacencia(adjacencia)
    teste = min(adjacencia,key=adjacencia.get)
    while teste in visitados:
        adjacencia.pop(teste)
        if len(adjacencia) == 0:
            return
        teste = min(adjacencia, key=adjacencia.get)
    return teste

priorityQueue = {}
resultantTree = {}
visitados = []
arvore = []

def geraArvoreMinima(verticeInicial):
    visitados.append(verticeInicial)
    menorAresta = getMenorArestaVertice(graph_lista[verticeInicial],visitados)
    arvore.append(menorAresta)
    if not menorAresta:
        return arvore
    return geraArvoreMinima(menorAresta)


verticeInicial = 'v1'
arvoreResultante = geraArvoreMinima(verticeInicial)
print(arvoreResultante)
    # findCloserVertice(priorityQueue[vert])
# print(priorityQueue)

