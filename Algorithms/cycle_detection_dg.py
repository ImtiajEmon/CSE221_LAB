# Cycle detection of directed graph using DFS

from collections import defaultdict
# This class represents a  graph using
# adjacency list representation

def check_cycle(u):
    dfs_visited[u] = 1
    visited[u] = 1

    
    for v in adj_lst[u]:
        
        if dfs_visited[v] == 0:
            check_cycle(v)

        if visited[v]:
            path_of_cycle.append(v) # Tracking the path of cycle
            return True

    visited[u] = 0
    return False



adj_lst = defaultdict(list)  # To represent graph
dfs_visited = [0] * int(1e5) 
visited = [0] * int(1e5)
path_of_cycle = []  


nodes = int(input())
edges = int(input())

# Taking the edges
for i in range(edges):
    u, v = input().split(' ')
    u = int(u)
    v = int(v)

    # For directed graph
    adj_lst[u].append(v)

flag = False
for u in range(1, nodes+1):
    if dfs_visited[u]:
        continue
    
    flag = check_cycle(u)

    if flag:
        break


if flag:
    print("The graph has a cycle\nThe nodes in cycle are:")

    path_of_cycle.append(path_of_cycle[0])
    path_of_cycle.reverse()
    print(path_of_cycle)
else:
    print("The graph has no cycle")
   