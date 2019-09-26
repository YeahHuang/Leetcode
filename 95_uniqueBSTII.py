# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n, left = 1 ) -> List[TreeNode]: 
        if left == n:
            return [TreeNode(n)]
        ret = []
        tmp = TreeNode(left)    #这里的特殊判断可以用下面的return [None, ] 来替换的
        for tr in self.generateTrees(n,  left+1):
            tmp.right = tr
            ret.append(tmp)
        tmp = TreeNode(n)
        for tl in self.generateTrees(n-1, left):
            tmp.left = tl
            ret.append(tmp)
        for i in range(left+1, n):
            for tl in self.generateTrees(i-1, left):
                for tr in self.generateTrees(n,  i+1):
                    tmp = TreeNode(i)
                    tmp.left, tmp.right = tl, tr
                    ret.append(tmp)
        return ret

class Solution:

    def generateTrees(self, n):
        return self.myGenerateTrees(1, n) if n>0 else []

    def myGenerateTrees(self, left, right  ) -> List[TreeNode]: #如果不存在n=0的情况的话 只需要下面这一段 还挺优雅的
        if left > right:
            return [None,]
        if left == right:
            return [TreeNode(right)]
        ret = []
        for i in range(left, right+1):
            for tl in self.myGenerateTrees(left, i-1):
                for tr in self.myGenerateTrees(i+1, right):
                    tmp = TreeNode(i)
                    tmp.left, tmp.right = tl, tr
                    ret.append(tmp)
        return ret

