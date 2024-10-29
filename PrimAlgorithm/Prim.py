from grafos.Grafos import graph_lista

def getMenorPeso(fila,visitadosList):
    menorPeso = float('inf')
    verticeMenorPeso = ''
    for vertice in fila:
        if fila[vertice]['peso'] < menorPeso and vertice not in visitadosList:
            menorPeso = fila[vertice]['peso']
            verticeMenorPeso = vertice
    return verticeMenorPeso

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
# resultado:
# {'v1': {'peso': 0, 'anterior': 0},
#  'v2': {'peso': 1, 'anterior': 'v1'},
#  'v3': {'peso': 2, 'anterior': 'v2'},
#  'v5': {'peso': 3, 'anterior': 'v2'},
#  'v6': {'peso': 1, 'anterior': 'v5'},
#  'v9': {'peso': 1, 'anterior': 'v5'},
#  'v4': {'peso': 2, 'anterior': 'v5'},
#  'v7': {'peso': 3, 'anterior': 'v4'},
#  'v8': {'peso': 2, 'anterior': 'v7'}}
