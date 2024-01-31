def quick_sort(arr, left, right):
    if left < right:
        mid = quick(arr, left, right)
        quick_sort(arr, left, mid - 1)
        quick_sort(arr, mid + 1, right)


def quick(arr, left, right):
    loc = left
    while left < right:
        while arr[loc] < arr[right]:
            right -= 1
        arr[right], arr[loc] = arr[loc], arr[right]
        loc = right

        while arr[left] < arr[loc]:
            left += 1
        arr[left], arr[loc] = arr[loc], arr[left]
        loc = left
    return loc


# Version-2
def quick_sort2(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort2(lesser) + [pivot] + quick_sort2(greater)


arr_list = [58, 62, 91, 43, 29, 37, 88, 72, 16, 30]
quick_sort(arr_list, 0, len(arr_list) - 1)
print(arr_list)

arr_list = [50, 20, 37, 91, 64, 18, 43, 59, 72, 81]
arr_list = quick_sort2(arr_list)
print(arr_list)
