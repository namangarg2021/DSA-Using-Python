def mod_bubble_sort(data_list):
    n = len(data_list)
    for i in range(n - 1):
        flag = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                flag = True
        if flag is False:
            break


arr = [24, 58, 11, 67, 92, 43]
mod_bubble_sort(arr)
print(arr)
