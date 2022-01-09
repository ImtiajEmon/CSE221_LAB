# Optional Task 3: Graph cycle detecting. Moreover it also give the path of cycle
# with adjacency list

from collections import defaultdict

def check_cycle(u):
    dfs_visited[u] = 1
    visited[u] = 1

    
    for v in adj_lst[u]:
        if dfs_visited[v] == 0:
            check_cycle(v)

        if visited[v]:
            return True

    visited[u] = 0
    return False



adj_lst = defaultdict(list)
dfs_visited = [0] * int(1e5)
visited = [0] * int(1e5)


Input = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 3\\optional_input_3.txt")
Output = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 3\\optional_output_3.txt", 'w')

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

flag = False
for u in range(1, nodes+1):
    if dfs_visited[u]:
        continue
    
    flag = check_cycle(u)

    if flag:
        break


if flag:
    Output.write("The graph has a cycle.")

else:
    Output.write("The graph has no cycle.")
   