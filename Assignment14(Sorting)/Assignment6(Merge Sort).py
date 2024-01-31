def merge_sort(arr, left, right):
    if left == right:
        return [arr[left]]
    mid = (left + right) // 2
    list1 = merge_sort(arr, left, mid)
    list2 = merge_sort(arr, mid + 1, right)
    return merge(list1, list2)


def merge(arr, brr):
    new_list = []
    i = 0
    j = 0
    while i < len(arr) and j < len(brr):
        if arr[i] > brr[j]:
            new_list.append(brr[j])
            j += 1
        else:
            new_list.append(arr[i])
            i += 1
    while i < len(arr):
        new_list.append(arr[i])
        i += 1
    while j < len(brr):
        new_list.append(brr[j])
        j += 1
    return new_list


arr_list = [72, 29, 83, 42, 16, 90, 56, 34, 20, 71, 88, 92, 7]
arr_list = merge_sort(arr_list, 0, len(arr_list) - 1)
print(arr_list)

arr_list = [50, 20, 37, 91, 64, 18, 43, 59, 72, 81]
arr_list = merge_sort(arr_list, 0, len(arr_list) - 1)
print(arr_list)
