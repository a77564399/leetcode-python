# Python TR
# Time：2021/8/13 12:16 上午
# coding = utf-8
class Solution(object):
    def reverseList(self, head):
        pre = None
        cur = head
        while cur is not None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre