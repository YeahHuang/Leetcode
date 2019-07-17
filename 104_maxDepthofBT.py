# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    #Sol1 recursion 40ms
    def maxDepth(self, root: TreeNode) -> int:
        if not root:    return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
    
    #Sol2 c++的tail recursion + BST

    #Sol3 iteration 48ms
    def maxDepth(self, root: TreeNode) -> int:
        stack = []
        if not root:    return 0
        stack.append((root,1))
        max_depth = 1
        while stack:
            tree, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if tree.left!=None:
                stack.append((tree.left, depth + 1))#一开始只写了一个() 以后注意一下元祖的语法细节咯
            if tree.right!=None:
                stack.append((tree.right, depth + 1))
        return max_depth