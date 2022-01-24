def LCS(i, j):
    if i < 0 or j < 0:
        return 0

    if memo[i][j] != -1:
        return memo[i][j]

    if s1[i] == s2[j]:
        memo[i][j] =  1 + LCS(i-1, j-1)
        link[i][j] = 3

    elif(LCS(i-1, j) > LCS(i, j-1)):
        memo[i][j] = LCS(i-1, j)
        link[i][j] = 1

    else:
        memo[i][j] = LCS(i, j-1)
        link[i][j] = 2

    return memo[i][j]

#=================================================================================================
zone = {'Y': "Yasnaya", 'P': "Pochinki", 'S': "School", 'R': "Rozhok", 'F': "Farm", 'M': "Mylta", 'H': "Shelter", 'I': "Prison"}

Input = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 6\\2_19201031_06\\Task_01_input.txt")
Output = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 6\\2_19201031_06\\Task_01_output.txt", 'w')

i = 1
s1 = ""
s2 = ""
n = 0

for line in Input:
    if i == 1:
        n = int(line)
    elif i == 2:
        s1 = line.strip()
    else:
        s2 = line.strip()
    i += 1
#=============================================================================
memo = [[-1 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
link = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]

Len = LCS(len(s1)-1, len(s2)-1)

common = ''
x = len(s1) - 1
y = len(s2) - 1
while x >= 0 and y >= 0:
    if link[x][y] == 1:
        x = x - 1

    elif link[x][y] == 2:
        y = y - 1

    else:
        common += s1[x]
        x = x - 1
        y = y - 1

corretness = (Len * 100) // n

for i in range(len(common)-1, -1, -1):
    Output.write(f"{zone[common[i]]} ")
Output.write("\n")

Output.write(f"Correctness of prediction: {corretness}%")
