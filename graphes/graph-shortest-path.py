def parse_graph(file):
    G = {}
    with open(file) as graph :
        for line in graph : 
            start, final, dist = line.rstrip().split(",")
            #print(f"(src)->(dist)->(dst)")
            if start not in G :
                G[start]={}
            G[start][final]=int(dist)
    return G

#print(parse_graph('reach.csv'))

def number_vertices(graph):
    nb = 0
    sommets = set()
    for s in graph.keys() : 
        if s not in sommets : 
            nb += 1 
            sommets.add(s)
        for i in graph[s].keys():
            if i not in sommets : 
                nb += 1
                sommets.add(i)
    return nb 

G = {'a': {'b': 7, 'd': 9, 'c': 14},
 'b': {'d': 10, 'e': 15},
 'c': {'d': 2, 'f': 9},
 'd': {'e': 11},
 'e': {'f': 6}}

M = {'a': {'b': 1, 'd': 1, 'c': 1}, 
'b': {'d': 1, 'e': 1}, 
'c': {'d': 1, 'f': 1}, 
'd': {'e': 1, 'a': 1}, 
'e': {'f': 1}, 
'f': {'e': 1}}

def reachables(graph, s):
    reach = set()
    for sommet in graph[s] : 
        reach.add(sommet)
#    for j in graph[sommet] : 
        for j in reachables(graph,sommet):        
            reach.add(j)
    return reach 
 # Je ne parviens pas à éviter de boucler à l'infini...

import math 
def shortest_distance(graph, v1, v2):

    # initialisation : on se définit une variable locale à la fonction qui matérialise le marquage

    visited = {}
    visited[v1]=0
    parents = {}
    # ensuite on fait une boucle jusqu'à ce que la condition soit remplie
    while True:

        # les arêtes qui satisfont le critère 
        edges = set()
        #on localise toutes les arêtes qui lient un noeud visité à un noeud non visité
        # on énumère toutes les arêtes, et on ajoute dans edges celles qui satisfont le critère
        for s_visited in visited.keys():
            if s_visited in graph: 
                for s in graph[s_visited].keys():
                    if s not in visited : 
                        edges.add((s_visited,s))
         

        # si on n'a aucune arête c'est que c'est raté
        if not edges:
            return None 

        # sinon on trouve la meilleure
        shortest_length = math.inf
        shortest_vertex = None
        for edge in edges:
             # trouver la plus courte et mémoriser le sommet correspondant
            if visited[edge[0]]+graph[edge[0]][edge[1]] < shortest_length :
                shortest_length = visited[edge[0]]+graph[edge[0]][edge[1]]
                shortest_vertex = edge[1]

        # marquer le sommet correspondant
        visited[shortest_vertex] = shortest_length
        # regarder si c'est le sommet 
        if shortest_vertex == v2:
            return shortest_length


def reversepath(source, start, end):
    v = end
    reversepath = [end]
    while v != start  :
        v = source[v]
        reversepath.append(v)
    return list(reversed(reversepath))

def shortest_path(graph, v1, v2):

    # initialisation : on se définit une variable locale à la fonction qui matérialise le marquage

    visited = {}
    visited[v1]=0
    source = {}

    # ensuite on fait une boucle jusqu'à ce que la condition soit remplie
    while True:

        # les arêtes qui satisfont le critère 
        edges = set()
        #on localise toutes les arêtes qui lient un noeud visité à un noeud non visité
        # on énumère toutes les arêtes, et on ajoute dans edges celles qui satisfont le critère
        for s_visited in visited.keys():
            if s_visited in graph: 
                for s in graph[s_visited].keys():
                    if s not in visited : 
                        edges.add((s_visited,s))
         

        # si on n'a aucune arête c'est que c'est raté
        if not edges:
            return None 

        # sinon on trouve la meilleure
        shortest_length = math.inf
        shortest_vertex = None
        shortest_edge = None 
        for edge in edges:
             # trouver la plus courte et mémoriser le sommet correspondant
            if visited[edge[0]]+graph[edge[0]][edge[1]] < shortest_length :
                shortest_length = visited[edge[0]]+graph[edge[0]][edge[1]]
                shortest_vertex = edge[1]
                shortest_edge = edge

        # marquer le sommet correspondant
        visited[shortest_vertex] = shortest_length
        source[shortest_vertex] = shortest_edge[0]
        # regarder si c'est le sommet 
        if shortest_vertex == v2:
            return shortest_length, reversepath(source, v1, v2)
    
print(shortest_path(G, 'a', 'f'))

# CORRECTION 
def reachable(graph, s):
    def reach_rec( graph, s, reached ): 
        if s not in reached : 
            reached.add(s)
            if s in graph:
                for i in graph[s]:
                    reached = reached | reach_rec(graph, i, reached)
    return reached 


