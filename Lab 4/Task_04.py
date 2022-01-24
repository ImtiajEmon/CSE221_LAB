from collections import defaultdict
from queue import PriorityQueue
# To get the max ele at top insert neg value

def dijkstra(source, nodes):
    for i in range(1, nodes+1):
        dist[i] = -inf

    dist[source] = inf

    pq = PriorityQueue()

    for node in range(1, nodes+1):
        pq.put((dist[node]*-1, node))  #(cost, node)

    while not pq.empty():
        pair = pq.get()
        cost = pair[0]*-1 
        u = pair[1]

        if dist[u] != cost:
            continue

        for adj_pair in adj_lst[u]:
            adj_cost = adj_pair[0]
            adj_node = adj_pair[1]
            temp = min(dist[u], adj_cost)

            if temp > dist[adj_node]:
                dist[adj_node] = temp
                pq.put((dist[adj_node]*-1, adj_node))

#-----------------------------------------------------
adj_lst = defaultdict(list)
dist = [0] * int(1e5)
inf = int(1e9 + 10)

Input = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 4\\input_4.txt")
Output = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 4\\output_4.txt", 'w')
string = Input.read()

tc = int(string[0])
lst = string.split("\n")

line = 1
while line < len(lst)-1:
    n, m = lst[line].split(' ')
    n = int(n)
    m = int(m)

    for i in range(line+1, line+m+1):
        u, v, d = lst[i].split(' ')
        u = int(u)
        v = int(v)
        d = int(d)
        adj_lst[u].append((d, v))
         
    source = int(lst[line+m+1].strip())
    line = line + m + 2
    
    dijkstra(source, n)

    for i in range(1, n+1):
        if dist[i] == inf:
            Output.write("0 ")
        elif dist[i] == -inf:
            Output.write("-1 ")
        else:
            Output.write(str(dist[i]) + ' ')
    Output.write("\n")
    