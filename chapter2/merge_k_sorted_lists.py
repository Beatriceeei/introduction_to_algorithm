# -*- coding:utf8 -*-

# 23. Merge k Sorted Lists
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def print_all(self):
        node = self
        while True:
            print node.val, "->",
            node = node.next
            if node is None:
                break
        print

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        tmp = head
        while True:
            if l1 is None:
                tmp.next = l2
                break
            elif l2 is None:
                tmp.next = l1
                break
            elif l1.val > l2.val:
                tmp.next = l2
                tmp = tmp.next
                l2 = l2.next
            else:
                tmp.next = l1
                tmp = tmp.next
                l1 = l1.next
        return head.next
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return
        length = len(lists)
        mid = length / 2
        if mid < length and mid:
            l1 = self.mergeKLists(lists[:mid])
            l2 = self.mergeKLists(lists[mid:length])
            l = self.mergeTwoLists(l1, l2)
            return l
        else:
            return lists[0]
# l1 = ListNode(2)
# l1.next = ListNode(6)
# l2 = ListNode(4)
# l2.next = ListNode(8)
# l3 = ListNode(1)
# l3.next = ListNode(5)
# l4 = ListNode(3)
# l4.next = ListNode(7)
# Solution().mergeKLists([l1,l2,l3,l4]).print_all()
# lists = [ListNode(i) for i in [2,6,4,8,1,5,3,7]]
Solution().mergeKLists([]).print_all()


