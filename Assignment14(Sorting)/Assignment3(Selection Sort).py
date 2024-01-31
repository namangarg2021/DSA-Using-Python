def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        ind = i
        for j in range(i + 1, n):
            if arr[ind] > arr[j]:
                ind = j
        arr[i], arr[ind] = arr[ind], arr[i]


arr_list = [38, 90, 47, 69, 52, 88, 71, 18, 20]
selection_sort(arr_list)
print(arr_list)
