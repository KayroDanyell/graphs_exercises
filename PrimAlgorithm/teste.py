from orca.punctuation_settings import infinity

graph_lista = {
    "v1": {"v1": 0, "v2": 1, "v3": 0, "v4": 0, "v5": 6, "v6": 5, "v7": 0, "v8": 0, "v9": 5},
    "v2": {"v1": 1, "v2": 0, "v3": 2, "v4": 0, "v5": 3, "v6": 1, "v7": 0, "v8": 5, "v9": 0},
    "v3": {"v1": 0, "v2": 2, "v3": 0, "v4": 5, "v5": 4, "v6": 0, "v7": 2, "v8": 0, "v9": 0},
    "v4": {"v1": 0, "v2": 0, "v3": 5, "v4": 0, "v5": 2, "v6": 0, "v7": 3, "v8": 6, "v9": 0},
    "v5": {"v1": 6, "v2": 3, "v3": 4, "v4": 2, "v5": 0, "v6": 4, "v7": 1, "v8": 4, "v9": 8},
    "v6": {"v1": 5, "v2": 1, "v3": 0, "v4": 0, "v5": 4, "v6": 0, "v7": 0, "v8": 0, "v9": 4},
    "v7": {"v1": 0, "v2": 0, "v3": 2, "v4": 3, "v5": 1, "v6": 0, "v7": 0, "v8": 9, "v9": 0},
    "v8": {"v1": 0, "v2": 5, "v3": 0, "v4": 6, "v5": 4, "v6": 0, "v7": 9, "v8": 0, "v9": 2},
    "v9": {"v1": 5, "v2": 0, "v3": 0, "v4": 0, "v5": 8, "v6": 4, "v7": 0, "v8": 2, "v9": 0}
}

def filterAdjacencia(adjacencia):
    return {k: v for k, v in adjacencia.items() if v != 0}
def getMenorArestaVertice(adjacencia,visitados):
    adjacencia = filterAdjacencia(adjacencia)
    teste = min(adjacencia, key=adjacencia.get)
    while teste in visitados:
        adjacencia.pop(teste)
        if len(adjacencia) == 0:
            return
        teste = min(adjacencia, key=adjacencia.get)
    return teste

def geraArvoreGeradoraMinima(priorityQueue,originalGraph):
    arvoreMinima={}
    for vertice in priorityQueue:
        menorAresta = priorityQueue[vertice]['menorAresta']
        arvoreMinima[menorAresta] =  originalGraph[menorAresta]
    return arvoreMinima

graph_dict = {"v1": {"v1": 0, "v2": 2, "v3": 3, "v4": 4, "v5": 3},
              "v2": {"v1": 1, "v2": 0, "v3": 4, "v4": 2, "v5": 2},
              "v3": {"v1": 2, "v2": 6, "v3": 0, "v4": 3, "v5": 4},
              "v4": {"v1": 3, "v2": 5, "v3": 2, "v4": 0, "v5": 2},
              "v5": {"v1": 3, "v2": 5, "v3": 2, "v4": 4, "v5": 0},
              }
priorityQueue = {}
for vert in graph_dict:
    vertice = graph_dict[vert]
    priorityQueue[vert] = {'peso': infinity, 'anterior': 0}


resultantTree = {}
visitados = []
for vert in graph_dict:
    visitados.append(vert)
    menorAresta = 0

    for vertAdjac in vertice:
        pesoAresta = vertice[vertAdjac]
        if pesoAresta > 0:
            priorityQueue[vert][vertAdjac] = pesoAresta

    menorAresta = getMenorArestaVertice(priorityQueue[vert], visitados)
    priorityQueue[vert]['menorAresta'] = menorAresta
arvore = geraArvoreGeradoraMinima(priorityQueue,graph_dict)
print('priorityQueue: ',priorityQueue)
print('arvere: ',arvore)

    # findCloserVertice(priorityQueue[vert])
# print(priorityQueue)

