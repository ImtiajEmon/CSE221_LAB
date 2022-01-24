from collections import defaultdict
from queue import PriorityQueue


def dijkstra(source, nodes):
    for i in range(1, nodes+1):
        dist[i] = 1e9 + 10

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
                link[adj_node] = u
                pq.put((dist[adj_node], adj_node))


#-----------------------------------------------------
adj_lst = defaultdict(list)
dist = [0] * int(1e5)
link = [0] * int(1e5)

Input = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 4\\input_2.txt")
Output = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 4\\output_2.txt", 'w')
string = Input.read()

tc = int(string[0])
lst = string.split("\n")

line = 1
while line < len(lst):
    n, m = lst[line].split(' ')
    n = int(n)
    m = int(m)

    for i in range(line+1, line+m+1):
        u, v, w = lst[i].split(' ')
        u = int(u)
        v = int(v)
        w = int(w)
        adj_lst[u].append((w, v))
        adj_lst[v].append((w, u))
    line = line + m + 1

    dijkstra(1, n)
    
    current = n
    path = []
    path.append(current)

    while current != 1:
        current = link[current]
        path.append(current)

    path.reverse()
    for node in path:
        Output.write(str(node) + ' ')
    Output.write("\n")