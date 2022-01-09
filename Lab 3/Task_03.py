# Task Task 3: Depth-First Search (DFS)
# with adjacency list

from collections import defaultdict

def dfs(u, stop):
    visited[u] = 1

    for v in adj_lst[u]:
        if visited[v]:
            continue
        
        if v not in path:
            path.append(v)

        dfs(v, stop)


adj_lst = defaultdict(list)
visited = [0] * int(1e5)
path = []

Input = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 3\\input_3.txt")
Output = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 3\\output_3.txt", 'w')

nodes = 0
edges = 0
i = 0
for line in Input:
    line = line.strip()
    if i == 0:
        nodes = int(line)

    elif i == 1:
        edges = int(line)

    else:
        u, v = line.split(' ')
        u = int(u)
        v = int(v)
        # For directed graph
        adj_lst[u].append(v)

    i += 1

start = 1
stop = 12
path.append(start)

if start == 1:
    start += 1


for u in range(1, nodes):
    if visited[u]:
        continue

    dfs(u, stop)

path.append(stop)


for city in path:
    Output.write(f"{city} ")
    if city == stop:
        break