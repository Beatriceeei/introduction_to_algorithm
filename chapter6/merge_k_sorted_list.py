# -*- coding:utf8 -*-

# 6.5-9 设计一个时间复杂度为nlgk的算法,将k个有序列表合并为一个有序列表,n是总元素个数
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def print_list(self):
        tmp = self
        while True:
            print tmp.val, "->",
            if not tmp.next:
                break
            tmp = tmp.next
        print

def generate_list(array):
    tail, head = ListNode(array[-1]), ListNode(array[-1])
    for i in xrange(len(array)-2,-1,-1):
        head = ListNode(array[i])
        head.next = tail
        tail = head
    return head

class Solution():
    @staticmethod
    def parent(i):
        return (i-1)/2
    @staticmethod
    def left(i):
        return 2*i+1
    @staticmethod
    def right(i):
        return 2*i+2
    @staticmethod
    def exchange(A, i, j):
        tmp = A[i]
        A[i] = A[j]
        A[j] = tmp
    def max_heapify(self, A, i):
        l, r, min = self.left(i), self.right(i), i
        if l < self.heap_size and A[l].val < A[min].val:
            min = l
        if r < self.heap_size and A[r].val < A[min].val:
            min = r
        if min != i:
            self.exchange(A, i, min)
            self.max_heapify(A, min)
    def build_min_heap(self, lists):
        # 最后一个结点偏移量是heap_size-1
        for i in xrange((self.heap_size-1)/2, -1, -1):
            self.max_heapify(lists, i)
    def merge(self, lists):
        self.heap_size = len(lists)
        self.build_min_heap(lists)
        while self.heap_size:
            print lists[0].val
            if lists[0].next:
                lists[0] = lists[0].next
            else:
                self.exchange(lists,0,self.heap_size-1)
                self.heap_size-=1
            self.max_heapify(lists,0)

head1 = generate_list([1,3,5])
head2 = generate_list([2,4,6])
head3 = generate_list([2,5,8])
A = [head1, head2, head3]
Solution().merge(A)