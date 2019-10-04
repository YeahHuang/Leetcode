class Solution:
    def distributeCoins(self, root):#48ms
        self.ans = 0
        
        def dfs(node):
            if not node: return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R - 1

        dfs(root)
        return self.ans


    def distributeCoins(self, root: TreeNode) -> int:#60ms
        return self.toBalance(root)[0]

    def toBalance(self, root) -> (int, int):
        
        if root is None:
            return (0,0)
        cur_cost, cur_balance =  tuple(map(lambda x,y: x+y,self.toBalance(root.left), self.toBalance(root.right)))
        cur_balance += root.val - 1
        return (cur_cost + abs(cur_balance), cur_balance)
        

'''
关于2个元组/list的依次相加 除了lambda x,y: x+y还可以用operator.add 60ms -> 56ms
        #import operator
        #tuple(map(operator.add, a, b))
'''