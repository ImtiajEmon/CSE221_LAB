def selection(arr, n):
    arr.sort()
    selected.append(arr[0])
    f = arr[0][0]

    for i in range(1, n):
        if arr[i][1] >= f:
            f = arr[i][0]
            selected.append(arr[i])

#================================================
arr = []
selected = []

Input = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 5\\Task_01_input.txt")
Output = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 5\\Task_01_output.txt", 'w')
lst = Input.read().split("\n")

n = int(lst[0])

for i in range(1, n+1):
    s, e = lst[i].split(' ')
    s = int(s)
    e = int(e)
    arr.append((e, s))

selection(arr, n)

Output.write(str(len(selected)))
for time in selected:
    Output.write(f"\n{time[1]} {time[0]}")