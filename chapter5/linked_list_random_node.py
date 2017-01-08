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
import random
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head


    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        result, cnt, node = None, 0, self.head
        while True:
            cnt += 1
            if random.randint(0, cnt) == 0:
                result = node.val
            node = node.next
            if not node:
                break
        if result == None:
            return self.getRandom()
        return result


l1 = ListNode(3)
for i in [2,1]:
   node = ListNode(i)
   node.next = l1
   l1 = node
l1.print_list()
# l1 = ListNode(1)
print Solution(l1).getRandom()
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()