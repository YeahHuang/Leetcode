# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        v = []
        def preTraverse(tree: TreeNode, depth: int):
            if tree is None:
                return
            if len(v) == depth:
                v.append([tree.val])
            else:
                if depth&1:
                    v[depth].insert(0, tree.val)
                else:
                    v[depth].append(tree.val)
            preTraverse(tree.left, depth + 1)
            preTraverse(tree.right, depth + 1)
        preTraverse(root, 0)
        return v #一开始蠢呼呼的写成了return preTraverse(root, 0)