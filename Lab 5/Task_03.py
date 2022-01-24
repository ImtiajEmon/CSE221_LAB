def compute(arr, seq, n):
    temp = []
    global ans
    global jacks_time
    global jills_time
    for i in seq:
        if i == 'J':
            temp.append(arr[0])
            ans += (arr[0])
            jacks_time += int(arr[0])
            arr.pop(0)
        else:
            ans += (temp[len(temp) - 1])
            jills_time += int(temp[len(temp) - 1])
            temp.pop()

arr = []
Input = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 5\\Task_03_input.txt")
Output = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 5\\Task_03_output.txt", 'w')
lst = Input.read().split("\n")

n = int(lst[0])
arr = lst[1].split(' ')
seq = lst[2]

arr.sort()

ans = ""
jacks_time = 0
jills_time = 0

compute(arr, seq, n)

Output.write(ans)
Output.write(f"\nJack will work for {jacks_time} hours")
Output.write(f"\nJill will work for {jills_time} hours")