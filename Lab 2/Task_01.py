def bubbleSort(arr):
    flag = True

    for i in range(len(arr)-1):              # For the best case array should be sorted
        for j in range(len(arr)-i-1):        # So, with flag I am keeping trac whether the array is
            if int(arr[j]) > int(arr[j+1]):  # sorted or not. If sorted then I am breaking the loop.
                flag = False                 # In that case the inner loop should execute n-1 times wich is O(n)
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
        if(flag):
            break


input_file = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 2\\input1.txt")
output_file = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 2\\output1.txt", 'w')

n = int(input_file.read(1))

s = input_file.read()
arr = s[1:].split(' ')

bubbleSort(arr)

for x in arr:
    output_file.write(x+" ")