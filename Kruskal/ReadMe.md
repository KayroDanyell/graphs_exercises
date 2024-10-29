# Algoritmo Kruskal:
### Descobrir arvore geradora Minima, ou seja, o subgrafo cuja soma das arestas é minimo e este grafo se mantenha conexo, porém inicia-se contruindo uma floresta e depois transforma em um grafo


* 1 - A partir dos vértices, criar uma lista de objetos, onde cada objeto contém um unico vertice 
* 2 - Criar um lista de arestas, e ordena-las de forma crescente de acordo com seu peso
* 3 - Para cada aresta, verificar se os Vertices adjacentes são do mesmo objeto
* 4 - se *não* forem do mesmo objeto, insira a aresta na arvore e faça um merge destes objetos