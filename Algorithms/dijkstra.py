# Shortest path  with adjacency list

from collections import defaultdict
from queue import PriorityQueue


def dijkstra(source, nodes):
    # make all distance to infinity
    for i in range(1, nodes+1):
        dist[i] = 1e9 + 10

    # make source distance 0
    dist[source] = 0

    pq = PriorityQueue()

    pq.put((0, source))  #(cost, node)

    while not pq.empty():
        pair = pq.get()
        cost = pair[0]
        u = pair[1]

        if dist[u] != cost:
            continue

        for adj_pair in adj_lst[u]:
            adj_cost = adj_pair[0]
            adj_node = adj_pair[1]

            if cost + adj_cost < dist[adj_node]:
                dist[adj_node] = cost + adj_cost
                pq.put((dist[adj_node], adj_node))


#-----------------------------------------------------
adj_lst = defaultdict(list)
dist = [0] * int(1e5)

nodes = int(input())
edges = int(input())

# Taking the edges with cost
for i in range(edges):
    u, v, cost = input().split(' ')
    u = int(u)
    v = int(v)
    cost = int(cost)

    # For undirected graph
    adj_lst[u].append((cost, v))
    adj_lst[v].append((cost, u))


dijkstra(1, nodes)

for v in range(1, nodes+1):
    print("Distance from 1"," to ", v, "= ", dist[v])
#--------------------------------------------------
'''5
6
1 2 2
1 3 10
2 3 5
2 5 3
3 4 3
4 5 1'''