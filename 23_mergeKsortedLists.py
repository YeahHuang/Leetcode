# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq #120ms C的才32ms 
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head, cur = ListNode(0), ListNode(0)
        head.next = cur
        t = []
        k = len(lists)
        heapq.heapify(t)
        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(t, (lists[i].val,i))
                lists[i] = lists[i].next
        #WA listcode object doesn't support indexing
        while t:
            num, idx = heapq.heappop(t)
            cur.next = ListNode(num)
            cur = cur.next
            if lists[idx] is not None:
                heapq.heappush(t, (lists[idx].val,idx))
                lists[idx] = lists[idx].next
        return head.next.next