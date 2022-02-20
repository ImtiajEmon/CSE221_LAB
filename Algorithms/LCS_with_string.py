#arr = [[0 for i in range(cols)] for j in range(rows)] // 2D array

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

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

memo = [[-1 for i in range(len(s2)+1)] for j in range(len(s1)+1)] 
link = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]

ans = LCS(len(s1)-1, len(s2)-1)

x = len(s1) - 1
y = len(s2) - 1

common = ''
while x >= 0 and y >= 0:
    if link[x][y] == 1:
        x = x - 1

    elif link[x][y] == 2:
        y = y - 1

    else:
        common += s1[x]
        x = x - 1
        y = y - 1

common = common[::-1] #reversed
print(ans)
print(common)
