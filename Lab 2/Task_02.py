def selection_sort(arr, n):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if int(arr[j]) < int(arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

input_file = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 2\\input2.txt")
output_file = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 2\\output2.txt", 'w')

INPUT = input_file.read()

n, m = INPUT[:3].split(' ')
n = int(n)
m = int(m)

arr = INPUT[4:].split(' ')

selection_sort(arr, n)

for i in range(m):
    output_file.write(arr[i] + ' ')


