def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2

    a1 = merge_sort(arr[:mid])
    a2 = merge_sort(arr[mid:])

    arr = merge(a1, a2)
    return arr

def merge(a1, a2):
    merged_arr = []

    i = 0
    j = 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            merged_arr.append(a1[i])
            i += 1
        else:
            merged_arr.append(a2[j])
            j += 1
        
    
    merged_arr += a1[i:]
    merged_arr += a2[j:]
    return merged_arr


arr = [9, 4, 5, 2, 1, 7, 4, 6]
arr = merge_sort(arr)
print(arr)
