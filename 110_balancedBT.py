# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.myBalanced(root)[1]
    def myBalanced(self, root) -> (int, bool): #returns max depth and whether balanced
        if root is None:
            return (0, True)
        d1, f1 = self.myBalanced(root.left)  #一次pass 但一开始这里又忘记写self.了
        d2, f2 = self.myBalanced(root.right)
        if f1 and f2 and abs(d1-d2)<=1:
            return(max(d1,d2)+1, True)
        else:
            return(-1, False)