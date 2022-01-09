def insertion_sort(arr_marks, n):
    for i in range(1, n):
        temp1 = arr_marks[i]
        temp2 = arr_id[i]

        j = i - 1
        while j >= 0 and int(arr_marks[j]) < int(temp1):
            arr_marks[j+1] = arr_marks[j]
            arr_id[j+1] = arr_id[j]
            
            j -= 1

        arr_marks[j+1] = temp1
        arr_id[j+1] = temp2

input_file = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 2\\input3.txt")
output_file = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 2\\output3.txt", 'w')

n = 0
arr_id = []
arr_marks = []

it = 0
for line in input_file:
    if it == 0:
        n = int(line.strip())
    elif it == 1:
        s = line.strip()
        arr_id = s.split(' ')
    elif it == 2:
        s = line.strip()
        arr_marks = s.split(' ')
    it += 1


insertion_sort(arr_marks, n)

for i in range(n):
    output_file.write(arr_id[i] + ' ')