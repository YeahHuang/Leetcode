# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #Sol1 recursive
    def pathSum(self, root: TreeNode, sum: int):
        if root is None:
            return []
        if root.left is None and root.right is None:
            if root.val == sum: #WA一次 直接改的时候忘记确认是否相等了 忘记写了这一行的判断
                return [[root.val]]
            else: #一开始else忘记写冒号了
                return [] 
        ret = []
        for path in (self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)):
            ret.append([root.val]+path)
        return ret
        

    #Sol2.1 我本来想的是 用多一个字符 记录它的father是什么 这样每次等于的时候 就回溯（省空间） 费时间 O(n)
    #Sol2.2 它这里每个节点多记一个目前路径(list) 这样等于的时候 再加入res。省时间 费空间(有点指数级增长的意思呀) referenced from @caikeke
def pathSum3(self, root, sum): 
    if not root:
        return []
    res = []
    queue = [(root, root.val, [root.val])]
    while queue:
        curr, val, ls = queue.pop(0)
        if not curr.left and not curr.right and val == sum:
            res.append(ls)
        if curr.left:
            queue.append((curr.left, val+curr.left.val, ls+[curr.left.val]))
        if curr.right:
            queue.append((curr.right, val+curr.right.val, ls+[curr.right.val]))
    return res
