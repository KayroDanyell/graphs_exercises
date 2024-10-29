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

def filterAdjacencia(adjacencia):
    return {k: v for k, v in adjacencia.items() if v != 0}
def getMenorPeso(fila,visitadosList):
    menorPeso = float('inf')
    verticeMenorPeso = ''
    for vertice in fila:
        if fila[vertice]['peso'] < menorPeso and vertice not in visitadosList:
            menorPeso = fila[vertice]['peso']
            verticeMenorPeso = vertice
    return verticeMenorPeso

graph_dict = {"v1": {"v1": 0, "v2": 2, "v3": 3, "v4": 4, "v5": 3},
              "v2": {"v1": 1, "v2": 0, "v3": 4, "v4": 2, "v5": 2},
              "v3": {"v1": 2, "v2": 6, "v3": 0, "v4": 3, "v5": 4},
              "v4": {"v1": 3, "v2": 5, "v3": 2, "v4": 0, "v5": 2},
              "v5": {"v1": 3, "v2": 5, "v3": 2, "v4": 4, "v5": 0},
              }
priorityQueue = {}
for vert in graph_lista:
    vertice = graph_lista[vert]
    priorityQueue[vert] = {'peso': float('inf'), 'anterior': 0}

verticeInicial = 'v1'
priorityQueue[verticeInicial]['peso'] = 0
arvore = {}
visitados = []

while len(priorityQueue) > 0:
    verticeMenorPeso = getMenorPeso(priorityQueue,visitados)
    visitados.append(verticeMenorPeso)
    arvore[verticeMenorPeso]=priorityQueue[verticeMenorPeso]
    priorityQueue.pop(verticeMenorPeso)
    adjacentesMenorPeso = graph_lista[verticeMenorPeso]

    for adjacente in adjacentesMenorPeso:

        if adjacentesMenorPeso[adjacente]<1 or adjacente not in priorityQueue:
            continue

        if adjacentesMenorPeso[adjacente] < priorityQueue[adjacente]['peso']:
            priorityQueue[adjacente]['anterior'] = verticeMenorPeso
            priorityQueue[adjacente]['peso'] = adjacentesMenorPeso[adjacente]

print(arvore)

{'v1': {'peso': 0, 'anterior': 0},
 'v2': {'peso': 1, 'anterior': 'v1'},
 'v3': {'peso': 2, 'anterior': 'v2'},
 'v5': {'peso': 3, 'anterior': 'v2'},
 'v6': {'peso': 1, 'anterior': 'v5'},
 'v9': {'peso': 1, 'anterior': 'v5'},
 'v4': {'peso': 2, 'anterior': 'v5'},
 'v7': {'peso': 3, 'anterior': 'v4'},
 'v8': {'peso': 2, 'anterior': 'v7'}}
