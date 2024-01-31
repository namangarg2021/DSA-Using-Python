# MAX HEAP

class Heap:
    def __init__(self):
        self.heap_list = []

    def create_heap(self, arr_list):
        i = 0
        for num in arr_list:
            self.insert(i, num)
            i += 1

    def insert(self, index, num):
        par_index = (index - 1) // 2
        if par_index < 0:
            self.heap_list.append(num)
            return
        temp = self.heap_list[par_index]

        if num > self.heap_list[par_index]:
            self.heap_list[par_index] = num
            self.insert(par_index, self.heap_list[par_index])
            self.heap_list[index] = temp
        else:
            self.heap_list.append(num)

    def top(self):
        if len(self.heap_list) == 0:
            raise EmptyHeapException()
        return self.heap_list[0]

    def delete(self):
        if len(self.heap_list) == 0:
            raise EmptyHeapException()
        index = len(self.heap_list) - 1
        temp = self.heap_list[index]
        max_val = self.heap_list[0]
        self.heap_list[0] = temp
        self.heap_list.pop(index)

        n = len(self.heap_list) - 1
        index = 0
        while True:
            left_child = (index * 2) + 1
            right_child = (index * 2) + 2

            if left_child > n and right_child > n:
                break

            if left_child <= n < right_child:
                if self.heap_list[left_child] >= temp:
                    self.heap_list[index] = self.heap_list[left_child]
                    self.heap_list[left_child] = temp
                break

            if self.heap_list[left_child] <= temp >= self.heap_list[right_child]:
                break

            if self.heap_list[left_child] > self.heap_list[right_child]:
                self.heap_list[index] = self.heap_list[left_child]
                self.heap_list[left_child] = temp
                index = left_child
            else:
                self.heap_list[index] = self.heap_list[right_child]
                self.heap_list[right_child] = temp
                index = right_child

        return max_val

    def heap_sort(self, list1):
        self.create_heap(list1)
        sorted_list = []

        try:
            while True:
                sorted_list.append(self.delete())
        except EmptyHeapException:
            pass
        return sorted_list


class EmptyHeapException(Exception):
    def __init__(self, msg="Empty Heap"):
        self.msg = msg

    def __str__(self):
        return self.msg


h = Heap()
arr = [40, 70, 10, 90, 60, 30, 50, 20, 80]
sorted_arr = h.heap_sort(arr)
print(sorted_arr)

arr = [34, 56, 12, 78, 43, 25, 10, 80, 60]
sorted_arr = h.heap_sort(arr)
print(sorted_arr)
