# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    #Sol1： 1st intuition 反向遍历 然后直接看二者是否相等 456ms
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
    
    def isSymmetric(self, root: TreeNode) -> bool:

        def traverse(tree: TreeNode, idx:int, tree_list:list):
            if not tree: return
            tree_list[idx] = tree.val
            if tree.left is not None:
                traverse(tree.left, idx*2+1, tree_list)
            if tree.right is not None:
                traverse(tree.right, idx*2+2, tree_list)

        def reverse_traverse(tree: TreeNode, idx:int, tree_list:list):
            if not tree: return
            tree_list[idx] = tree.val
            if tree.left is not None:
                reverse_traverse(tree.left, idx*2+2, tree_list)
            if tree.right is not None:
                reverse_traverse(tree.right, idx*2+1, tree_list)

        if not root: return True
        depth = self.maxDepth(root)
        MAX_INF = 2**32-1
        tree_left =[MAX_INF for i in range(2**(depth-1))]
        tree_right =[MAX_INF for i in range(2**(depth-1))]
        traverse(root.left,0, tree_left)
        reverse_traverse(root.right, 0, tree_right)
        return tree_left == tree_right

    #Sol2: standard recursion 搞清楚symmetric的程序语言就好 可以有很多提前的剪枝 就很优秀吖 40ms 
    def isSymmetric(self, root: TreeNode) -> bool:

        def isMirror(tree1: TreeNode, tree2: TreeNode):
            if not tree1 and not tree2: return True
            if (not tree1 and tree2) or (not tree2 and tree1):  return False
            return tree1.val==tree2.val and isMirror(tree1.left, tree2.right) and isMirror(tree1.right, tree2.left)

        if not root: return True
        return isMirror(root.left, root.right)

    #Sol3: standard iteration 52ms
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = []
        if not root: return True
        stack.append([root,root])
        flag = True
        while stack:
            tree1, tree2 = stack.pop()
            if not tree1 and not tree2: continue
            if (not tree1 and tree2) or (not tree2 and tree1):
                flag = False
                break
            if tree1.val == tree2.val:
                stack.append((tree1.left, tree2.right))
                stack.append((tree1.right, tree2.left))
            else:
                flag = False
                break
        return flag