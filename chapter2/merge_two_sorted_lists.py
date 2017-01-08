# -*- coding:utf8 -*-

# 21. Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def print_all(self):
        node = self
        while True:
            print node.val,"->",
            node = node.next
            if node is None:
                break
        print

# brillant answer
# def mergeTwoLists(self, l1, l2):
#     current = head = ListNode(0)
#     while l1 and l2:
#         if l1.val <= l2.val:
#             current.next = l1
#             l1 = l1.next
#         else:
#             current.next = l2
#             l2 = l2.next
#         current = current.next
#     current.next = l1 or l2
#     return head.next



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

# l1 = ListNode(8)
# for i in [6,4,2]:
#    node = ListNode(i)
#    node.next = l1
#    l1 = node
l1 = ListNode(0)

l2 = ListNode(7)
for i in [5,3,1]:
   node = ListNode(i)
   node.next = l2
   l2 = node
l1.print_all()
l2.print_all()


# Solution().mergeTwoLists(l1, l2).print_all()
Solution().mergeTwoLists(l1, l2).print_all()