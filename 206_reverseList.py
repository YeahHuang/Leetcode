# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(head: ListNode) -> ListNode:
            if head == None or head.next == None:
                return head
            else:
                l = reverse(head.next)
                qpp = l
                while qpp.next!=None:
                    qpp = qpp.next
                qpp.next = ListNode(head.val)
                return l
        return reverse(head)

'''

'''
    def reverseList(self,head): #iterative
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def reverseList(self, head):#iterative
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

    def reverseList(self,head, prev=None):#recursive
        if not head:
            return prev
        curr, head.next = head.next, prev
        return self.reverseList(curr, head)

