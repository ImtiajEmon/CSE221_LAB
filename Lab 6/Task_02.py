def LCS(i, j, a, b):
    if i < 0 or j < 0:
        return 0

    if memo[i][j] != -1:
        return memo[i][j]

    if a[i] == b[j]:
        memo[i][j] =  1 + LCS(i-1, j-1, a, b)
        link[i][j] = 3

    elif(LCS(i-1, j, a, b) > LCS(i, j-1, a, b)):
        memo[i][j] = LCS(i-1, j, a, b)
        link[i][j] = 1

    else:
        memo[i][j] = LCS(i, j-1, a, b)
        link[i][j] = 2

    return memo[i][j]

#=================================================================================================
zone = {'Y': "Yasnaya", 'P': "Pochinki", 'S': "School", 'R': "Rozhok", 'F': "Farm", 'M': "Mylta", 'H': "Shelter", 'I': "Prison"}

Input = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 6\\2_19201031_06\\Task_02_input.txt")
Output = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 6\\2_19201031_06\\Task_02_output.txt", 'w')

i = 1
s1 = ""
s2 = ""
s3 = ""

for line in Input:
    if i == 1:
        s1 = line.strip()
    elif i == 2:
        s2 = line.strip()
    else:
        s3 = line.strip()
    i += 1
#=============================================================================
memo = [[-1 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
link = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]

Len1 = LCS(len(s1)-1, len(s2)-1, s1, s2)

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

common = common[::-1]

memo = [[-1 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
Len2 = LCS(len(common)-1, len(s3)-1, common, s3)
ans = min(Len1, Len2)

Output.write(f"{ans}")