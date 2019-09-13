 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: #52ms

    def __init__(self):
        self.opt = []
        self.neg = []

    def verticalTraversal(self, root: TreeNode):
        self.myVerticalTraversal(root, 0, 0)
        tmp = self.neg[::-1] + self.opt
        ret = []
        for i,x in enumerate(tmp): #一开始没有读懂题目细节 包括bottom-down + value重叠
            x.sort()
            ret.append([])
            for xx in x:
                ret[i].append(xx[1])
        return ret
    
    def myVerticalTraversal(self, tree: TreeNode, x:int, y:int):
        if tree is None: #不如 if tree:
            return
        if x >= 0:
            if x == len(self.opt):
                self.opt.append([(y, tree.val)])
            else:
                self.opt[x].append((y, tree.val))
        else:
            if -x-1 == len(self.neg):
                self.neg.append([(y, tree.val)])
            else:
                self.neg[-x-1].append((y, tree.val))
        self.myVerticalTraversal(tree.left, x-1, y+1)
        self.myVerticalTraversal(tree.right,x+1, y+1)


#Improved 1: collections.defaultdict(list) 来代替前面的neg&pos 
class Solution:

    def __init__(self):
        self.list = collections.defaultdict(list)

    def verticalTraversal(self, root: TreeNode):
        self.myVerticalTraversal(root, 0, 0)
        ret = [[] for _ in range(len(self.list))]
        ordered = collections.OrderedDict(sorted(self.list.items())) #这一行的order可以不用 直接带入下面 44ms->32ms
        i = 0
        for i, (x, tmp) in enumerate(ordered.items()): #这一行的语法纠结了很久。 注意 所有dict下面的都需要dict.items() 才可以for k,v 的遍历
            tmp.sort()
            for (y, val) in tmp:
                ret[i].append(val)
            i += 1
        return ret

    def myVerticalTraversal(self, tree: TreeNode, x:int,  y:int):
        if tree:
            self.list[x].append((y, tree.val))
            self.myVerticalTraversal(tree.left, x-1, y+1)
            self.myVerticalTraversal(tree.right,x+1, y+1)

#Improved2 进一步改进代码

    def verticalTraversal(self, root: TreeNode): #32/36ms beats 90%
        self.myVerticalTraversal(root, 0, 0)
        return [[val for y,val in sorted(tmp)] for x,tmp in sorted(self.list.items())] 
        #真的没想到有一天我也可以写出这样的酷酷代码哈哈哈 快乐！！！
       


