def partition(arr, l, r):
    pivot = arr[l] #we take 1st element as pivot
    i = l
    j = l+1

    while(j <= r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
        else:
            j += 1

    arr[l], arr[i] = arr[i], arr[l]

    return i


def quick_sort(arr, start, end):
    if start >= end:
        return
    else:
        p = partition(arr, start, end)
        quick_sort(arr, start, p-1)
        quick_sort(arr, p+1, end)

arr = [10, 15, 15, 20, 5]
quick_sort(arr, 0, len(arr)-1)
print(arr)
