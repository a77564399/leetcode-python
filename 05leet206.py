# Python TR
# Time：2021/8/13 12:04 上午
# coding = utf-8
class Solution(object):
    def reverseList(self, head):
        if head == None:
            return head
        LinkedList = ListNode()
        LinkedList.next = head
        ele = head.next
        while ele is not None:
            x = ele
            x.next = LinkedList.next
            LinkedList.next=x
            ele = ele.next
        return LinkedList.next
