# Python TR
# Time：2021/8/12 10:26 下午
# coding = utf-8
class Solution(object):
    def removeElements(self, head, val):
        ele = head.next()
        while ele!=None:
            if ele.next and ele.next.val==val:
                ele.next = ele.next.next
            ele = ele.next
        return ele

    if __name__ == '__main__':
        head = [1, 2, 6, 3, 4, 5, 6]
        val = 6
        print(removeElements(object,head,val))

class Solution(object):
    def removeElements(self, head, val):
        if head == None:
            return head
        first = ListNode()
        first.next = head
        ele = first
        while ele != None:
            if ele.next and ele.next.val == val:
                ele.next = ele.next.next
            else:
                ele = ele.next
        return first.next