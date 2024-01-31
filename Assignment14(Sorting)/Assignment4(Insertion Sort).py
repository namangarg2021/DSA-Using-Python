def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i - 1
        temp = arr[i]
        while j >= 0:
            if arr[j] > temp:
                arr[j + 1] = arr[j]
            else:
                break
            j -= 1
        arr[j + 1] = temp


arr_list = [50, 20, 37, 91, 64, 18, 43, 59, 72, 81]
insertion_sort(arr_list)
print(arr_list)
