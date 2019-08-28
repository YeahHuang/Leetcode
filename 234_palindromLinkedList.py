class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow,  rev, slow.next

        if fast:
            # fast is at the end, move slow one step further for comparison(cross middle one)
            slow = slow.next

        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        # if equivalent then rev become None, return True; otherwise return False 
        return not rev 