# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        return self.myMaxPathSum(root)[0]

    #88ms faster than 98% 棒！
    def myMaxPathSum(self, root): #returns 2 values: maxPathSum, maxPathSum that ends with root
        if root is None: #WA一次 因为没有考虑None的情况 直接return(0,0) 是不行的 return int(float('-inf')) 也是不符合规范的
            return (float('-inf'), float('-inf')) 
        if root.left is None and root.right is None:
            return (root.val, root.val)
        max_l, max_ends_l = self.myMaxPathSum(root.left)
        max_r, max_ends_r = self.myMaxPathSum(root.right)
        max_ends_root = max(root.val, max_ends_l+root.val, max_ends_r+root.val)
        max_sum = max(max_l, max_r, max_ends_root, max_ends_l+max_ends_r+root.val)
        return (max_sum, max_ends_root) #情况比较多， 索性把代码整理清楚后就发现了自己的漏洞 不错