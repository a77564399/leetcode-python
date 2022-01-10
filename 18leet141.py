# Python TR
# Time：2021/8/23 10:32 上午
# coding = utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l = ListNode()
        l.next = head
        f = ListNode()
        f.next = head
        while f.next != None and f.next.next!=None:
            l = l.next
            f = f.next.next
            if l==f:
                return True
        return False