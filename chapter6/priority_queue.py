# -*- coding:utf8 -*-

class MininumPriorityQueue():
    def __init__(self, A):
        self.heap_size = len(A)
        self.heap = A
    @staticmethod
    def parent(i):
        return (i-1)/2
    @staticmethod
    def left(i):
        return 2*i+1
    @staticmethod
    def right(i):
        return 2*i+2
    def print_heap(self):
        print self.heap[:self.heap_size]
    def swp(self, i, j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp
    def min_heapify(self, i):
        l, r = self.left(i), self.right(i)
        if l < self.heap_size and self.heap[l] < self.heap[i]:
            smallest = l
        else:
            smallest = i
        if r < self.heap_size and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.swp(i, smallest)
            self.min_heapify(smallest)
    def build_min_heap(self):
        for i in xrange((self.heap_size-1)/2, -1, -1):
            self.min_heapify(i)
    def minimum(self):
        if self.heap_size == 0:
            print "heap size is 0"
            return
        return self.heap[0]
    def extract_min(self):
        if self.heap_size == 0:
            print "heap size is 0"
            return
        mininum = self.heap[0]
        self.swp(0, self.heap_size-1)
        self.min_heapify(0)
        self.heap_size-=1
        return mininum
    def increase_key(self, key):
        self.heap_size += 1
        self.heap[-1] = key
        i = self.heap_size-1
        while True:
            if self.parent(i)<0:
                break
            if self.heap[i] < self.heap[self.parent(i)]:
                self.swp(i, self.parent(i))
                i = self.parent(i)
            else:
                break
    def remove(self, i):
        self.swp(i, self.heap_size-1)
        self.min_heapify(i)
        self.heap_size -= 1

A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
queue = MininumPriorityQueue(A)
queue.build_min_heap()
queue.print_heap()
print queue.extract_min()
queue.print_heap()
queue.increase_key(1)
queue.print_heap()
queue.remove(2)
queue.print_heap()