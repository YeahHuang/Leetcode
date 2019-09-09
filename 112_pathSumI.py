# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #Sol1 recursive
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None: #WA 因为一开始默认[] sum=0 也是true的 可是其实题目的预定义不是这样的。 如果在面试的情况下需要注意和面试官提前确认好 
            return False
        if root.left is None and root.right is None:
            return root.val == sum  
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
        #一开始笔误 ⬆️忘记写self.hasXXX 而且错误的写成了self.left 而不是root.left 以后需要更熟练

    #Sol2 iterative reference from @112's solution 应该还挺好理解滴 
    class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        de = [(root, sum - root.val), ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:  
                return True
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        return False
