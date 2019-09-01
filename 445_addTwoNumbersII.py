# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def add(l1, l2, len1, len2) -> (ListNode, int):
            if len1 == len2:
                if len1==0:
                    summ, carry = None, 0
                else:
                    next_summ, carry = add(l1.next, l2.next, len1-1, len2-1)
                    summ = ListNode((l1.val+l2.val+carry)%10)
                    summ.next = next_summ
                    carry = (l1.val+l2.val+carry)//10
            elif len1>len2:
                next_summ, carry = add(l1.next, l2, len1-1, len2)
                summ = ListNode((l1.val + carry)%10)
                summ.next = next_summ
                carry = (l1.val + carry)//10
            else:
                next_summ, carry = add(l1, l2.next, len1, len2-1)
                summ = ListNode((l2.val+carry)%10) 
                summ.next = next_summ
                carry = (l2.val + carry)//10 #这里可以用carry, summ.val = divmod(l2.val+carry, 10)
            
            return (summ, carry)

        summ, carry = add(l1, l2, self.getLen(l1), self.getLen(l2))
        if carry == 1:
            ret = ListNode(1)
            ret.next = summ
        else:
            ret = summ
        return ret

    def getLen(self, l: ListNode):
        length = 0
        while l is not None:
            length += 1
            l = l.next
        return length

    #@yuzhoul Stack 不用dfs
    class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Use two stacks to store the number
        stack1 = []
        stack2 = []
        ptr = l1
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        ptr = l2
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        carry = 0
        result = []
        head = ListNode(-1)
        while stack1 or stack2:
            if not stack1:
                val = stack2.pop()
            elif not stack2:
                val = stack1.pop()
            else:
                val = stack1.pop() + stack2.pop()    
            carry, val = divmod(carry + val, 10)
            head.val = val
            temp = head
            head = ListNode(-1)
            head.next = temp
        if carry: head.val = carry
        return head if head.val != -1 else head.next