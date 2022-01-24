def selection(arr, n, m):
    arr.sort()
    selected[0] = arr[0][0]
    cnt[0] += 1

    for i in range(1, n):
        for j in range(m):
            if arr[i][1] >= selected[j] or selected[j] == 100000000:
                selected[j] = arr[i][0]
                cnt[j] += 1
                break
                

#================================================
arr = []
Input = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 5\\Task_02_input.txt")
Output = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 5\\Task_02_output.txt", 'w')
lst = Input.read().split("\n")

n, m = lst[0].split(' ')
n = int(n)
m = int(m)

for i in range(1, n+1):
    s, e = lst[i].split(' ')
    s = int(s)
    e = int(e)
    arr.append((e, s))

selected = [100000000] * m
cnt = [0] * m

selection(arr, n, m)

total = 0
for c in cnt:
    total += c

Output.write(str(total))