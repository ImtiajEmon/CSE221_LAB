# Task 1: Graph Building
# with adjacency list

from collections import defaultdict

adj_lst = defaultdict(list)

Input = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 3\\input_1.txt")
Output = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 3\\output_1.txt", 'w')

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

for u in range(1, nodes+1):
    Output.write(f"{u} -> {adj_lst[u]}\n")