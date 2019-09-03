# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #Sol1 recursive 40ms
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    
    #Sol2 iterative 36ms
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        ret = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            tmp_node = stack.pop()
            ret.append(tmp_node.val)
            root = tmp_node.right
        return ret

    #Sol3 Morris Traversal 可以节省空间 且时间复杂度还是O(n)
    #大概就是旋转一下 如果有左节点 就把cur = root.left 然后把root连接到cur.right后面去
    #参见 https://leetcode.com/problems/binary-tree-inorder-traversal/solution/