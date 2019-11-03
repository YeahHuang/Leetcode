# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        boundary = [root.val]
        if root.left:
            cur = root.left
            while cur and (cur.left or cur.right):
                boundary.append(cur.val)
                if cur.left:
                    cur = cur.left
                else:
                    cur = cur.right
        #print(boundary)                

        def dfs(root):
            #print(root.val)
            if root.left is None and root.right is None:
                boundary.append(root.val)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
                
        #print(boundary)
        if root.left or root.right: #WA 没考虑[1]
            dfs(root)
        insert_idx = len(boundary)
        if root.right and (root.right.left or root.right.right):
            cur = root.right
            while cur and (cur.left or cur.right):
                boundary.insert(insert_idx, cur.val)
                if cur.right:
                    cur = cur.right
                else:
                    cur = cur.left

                
        return boundary