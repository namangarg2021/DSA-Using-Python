def bubble_sort(data_list):
    n = len(data_list)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data_list[j] > data_list[j + 1]:
                data_list[j + 1], data_list[j] = data_list[j], data_list[j + 1]


arr = [24, 58, 11, 67, 92, 43]
bubble_sort(arr)
print(arr)
