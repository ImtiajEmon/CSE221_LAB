# DSU only work for undirected graph

def makeset(u):
    master[u] = u
    size[u] = u
    
def find(u):
    if master[u] == u:
        return u
    master[u] = find(master[u]) # Huristic 1: path compression
    return master[u]
    
def unite(u, v):
    u = find(u)
    v = find(v)
    
    if u == v:
        return False
    
    if size[u] > size[v]:  # Huristic 2: unite by size
        master[v] = u
        size[u] += size[v]
    else:
        master[u] = v
        size[v] = size[u]
        
    return True
#=========================================

nodes, edges = map(int, input("Enter the number of nodes and edges: ").split())

master = [0] * (nodes+1)
size = [0] * (nodes+1)

#making everyone's master itself and size 1
for i in range(1, nodes+1):
    makeset(i)
    
for i in range(edges):
    u, v = map(int, input().split())
    
    flag = unite(u, v)
    if flag:
        print("The edges were in different component")
    else:
        print("The edges are in same component")
        