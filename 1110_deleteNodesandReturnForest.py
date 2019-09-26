# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.to_delete = set()
        self.forests = {}
        
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        def dfs(tree):
            if tree is None:
                return
            if tree.val in self.to_delete:
                self.to_delete.remove(tree.val) 
                if tree.left:
                    if tree.left.val not in self.to_delete: #WA一次 忘记写这个判断条件了
                        self.forests[tree.left.val] = None
                    dfs(tree.left)
                if tree.right:
                    if tree.right.val not in self.to_delete:
                        self.forests[tree.right.val] = None
                    dfs(tree.right)
                return 
            else:
                ret = TreeNode(tree.val)
                ret.left = dfs(tree.left)
                ret.right = dfs(tree.right)
                if ret.val in self.forests:
                    self.forests[ret.val] = ret
            return ret
        
        self.to_delete = set(to_delete)
        if root.val not in self.to_delete:
            self.forests[root.val] = None
        dfs(root)
        return [v for k, v in self.forests.items()]

    #Improved: 92ms -> 76ms 稍微省了一咩咩空间14.4M->14.3M
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        forests = []
        def dfs(tree:TreeNode, parent_deleted:bool):
            if tree is None:
                return
            if tree.val in to_delete:
                to_delete.remove(tree.val) 
                if tree.left:
                    dfs(tree.left, True)
                if tree.right:
                    dfs(tree.right, True)
                return 
            else:
                ret = TreeNode(tree.val)
                ret.left = dfs(tree.left, False)
                ret.right = dfs(tree.right, False)
                if parent_deleted:
                    forests.append(ret)
            return ret
        dfs(root, True)
        return forests
