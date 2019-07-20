# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    #Sol1 自己直接排序 96ms #这样虽然效率还行 但你应该知道其实并不符合这个下面demo的逻辑bia
    def __init__(self, root: TreeNode):

        def tree2list(tree:TreeNode):
            if tree is None:
                return []
            return tree2list(tree.left) + [tree.val] + tree2list(tree.right)

        self.nums = tree2list(root)
    

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.nums.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.nums)

    #Sol2 真的根据它需要的顺序来排
    #Referenced from @Stefan and @clue's solution
    def __init__(self, root: TreeNode):
        self.stack = []
        self.pushAll(root)

    def next(self) -> int:
        tree = self.stack.pop()
        self.pushAll(tree.right)
        return tree.val

    def hasNext(self) -> bool:
        return self.stack

    def pushAll(self,tree): #这样一个个的push
        if not tree: return
        self.stack.append(tree)
        while tree.left is not None:
            self.stack.append(tree.left)
            tree = tree.left

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()