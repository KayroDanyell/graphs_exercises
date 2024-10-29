from grafos.Grafos import graph_lista

arvore = {}

objetos = []
for vertice in graph_lista:
    objetos.append([vertice])

arestas = []
for vertice in graph_lista:
    adjacentes = graph_lista[vertice]
    for adjacente in adjacentes:
        if adjacentes[adjacente] > 0:
            arestas.append({'saida': vertice, 'chegada': adjacente, 'peso': adjacentes[adjacente]})
arestas = sorted(arestas, key=lambda d: d['peso'])


def findVerticeObjIndex(vert, objetos):
    for obj in objetos:
        if vert in obj:
            return objetos.index(obj)


counter = 0
for aresta in arestas:
    objVerticeSaida = findVerticeObjIndex(aresta['saida'], objetos)
    objVerticeChegada = findVerticeObjIndex(aresta['chegada'], objetos)
    if aresta['saida'] not in objetos[objVerticeChegada]:
        arvore[aresta['saida'] + ' - ' + aresta['chegada']] = aresta
        objetos[objVerticeChegada] = objetos[objVerticeChegada] + objetos[objVerticeSaida]
        del objetos[objVerticeSaida]
    counter += 1

print(objetos)
print(arestas)
print(arvore)

{
'v1 - v2': {'saida': 'v1', 'chegada': 'v2', 'peso': 1},
'v5 - v6': {'saida': 'v5', 'chegada': 'v6', 'peso': 1},
'v5 - v9': {'saida': 'v5', 'chegada': 'v9', 'peso': 1},
'v2 - v3': {'saida': 'v2', 'chegada': 'v3', 'peso': 2},
'v4 - v5': {'saida': 'v4', 'chegada': 'v5', 'peso': 2},
'v7 - v8': {'saida': 'v7', 'chegada': 'v8', 'peso': 2},
'v2 - v5': {'saida': 'v2', 'chegada': 'v5', 'peso': 3},
'v4 - v7': {'saida': 'v4', 'chegada': 'v7', 'peso': 3}
}
