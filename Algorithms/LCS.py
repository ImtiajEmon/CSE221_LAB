#arr = [[0 for i in range(cols)] for j in range(rows)] // 2D array

def LCS(i, j):
    if i < 0 or j < 0:
        return 0

    if memo[i][j] != -1:
        return memo[i][j]

    elif s1[i] == s2[j]:
        memo[i][j] =  1 + LCS(i-1, j-1)

    else:
        memo[i][j] =  max(LCS(i-1, j), LCS(i, j-1))

    return memo[i][j]

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

memo = [[-1 for i in range(len(s2)+1)] for j in range(len(s1)+1)] 

ans = LCS(len(s1)-1, len(s2)-1)
print(ans)
