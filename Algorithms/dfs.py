# dfs with adjacency list

from collections import defaultdict
# This class represents a directed graph using
# adjacency list representation

def dfs(u):
    visited[u] = 1

    for v in adj_mtx[u]:
        if visited[v]:
            continue
        print(f"Going {u} to {v}") #To see what actually happend (aditional line)
        dfs(v)

#-----------------------------------------------------
adj_mtx = defaultdict(list)
visited = [0] * int(1e5)

nodes = int(input())
edges = int(input())

# Taking the edges
for i in range(edges):
    u, v = input().split(' ')
    u = int(u)
    v = int(v)

    # For undirected graph
    adj_mtx[u].append(v)
    adj_mtx[v].append(u)


for u in range(1, nodes+1, 1):
    if visited[u]:
        continue

    dfs(u)
#--------------------------------------------------
