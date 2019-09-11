# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #Sol1 recursive 36ms
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)

    #Sol2 iterative deque 36ms
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p,q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            return p.val == q.val
        
        deq = collections.deque([(p,q),])
        is_same = True
        while deq:
            p, q = deq.popleft()
            if not check(p,q):
                is_same = False
                break
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        return is_same