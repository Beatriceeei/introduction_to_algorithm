# -*- coding:utf8 -*-
def parent(i):
    return (i-1)/2

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

class HeapSort():

    # 维护堆的性质
    def max_heapify(self, A, i):
        length, largest = self.heap_size, None
        l, r = left(i), right(i)
        if l < length and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r < length and A[r] > A[largest]:
            largest = r
        if i != largest:
            tmp = A[i]
            A[i] = A[largest]
            A[largest] = tmp
            self.max_heapify(A, largest)
        return A

    # A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    # print max_heapify(A, 2)

    # 建堆
    def build_max_heap(self, A):
        for i in xrange((self.heap_size-1)/2,-1,-1):
            self.max_heapify(A, i)
        return A

    # A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    # print build_max_heap(A)
    #
    # 排序
    def heap_sort(self,A):
        self.heap_size = length = len(A)
        self.build_max_heap(A)
        for i in xrange(length-1, -1, -1):
            tmp = A[0]
            A[0] = A[i]
            A[i] = tmp
            self.heap_size -= 1
            self.max_heapify(A, 0)
        return A

A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
print HeapSort().heap_sort(A)