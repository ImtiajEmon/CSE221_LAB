# Optional Task 1 

from collections import defaultdict
# This class represents a  graph using
# adjacency list representation

def bfs(u, start, stop):
    flag = False
    visited[u] = 1

    queue = []
    queue.append(u)
    
    while len(queue) != 0:
        frnt = queue[0]
        queue.pop(0)

        for v in adj_lst[frnt]:
            if visited[v]:
                continue

            if v == start:
                flag = True
            if v == stop:
                flag = False
            if flag and  v not in path:
                path.append(v)

            queue.append(v)
            visited[v] = 1


adj_lst = defaultdict(list)
visited = [0] * int(1e5)
path = []
path_map = {1:"Pallet Town", 2:"Cerulean City ", 3:"Celadon City", 4:"Lavender Town", 5:"Viridian City", 6:"Cinnabar Island", 7:"Fuchsia City", 8:"Safari Zone", 9:"Team Rocket’s Lair", 10:"Indigo Plateau", 11:"Pewter City", 12:"Victory Road"}

Input = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 3\\optional_input_1.txt")
Output = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 3\\optional_output_1.txt", 'w')

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

    bfs(u, start, stop)

path.append(stop)

#cities = 
for i in range(len(path)):
    if i == len(path) - 1:
        Output.write(f"{path_map[path[i]]}")
    else:
        Output.write(f"{path_map[path[i]]} -> ")