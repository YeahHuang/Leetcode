# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        
        #TLE 虽然O(n) 怀疑是数组拷贝的锅
        #但是看了自己的104_maxDepthofBST后发现明明是 recursive 快于 iterative吖 
        #后来发现 孩子次数 = 父亲次数 * 2 到底下其实是指数级的了吖～～  每个 1 * 2^n 所以一共*2
        def rob(tree:TreeNode, can_contain: bool) -> int:   
            ans = 0
            if tree is not None:
                ans = rob(tree.left, True)+rob(tree.right, True)
                if can_contain:
                    ans = max(ans, rob(tree.left, False)+rob(tree.right, False)+tree.val)
            return ans


        return rob(root, True)

        #Refined Sol:   52ms
        def rob(tree: TreeNode) -> list:
            #0 not contains 1 contain
            ans = [0, 0]
            if tree is not None:
                left, right = rob(tree.left), rob(tree.right)
                ans[0] = left[1] + right[1]     #欲速则不达啊！谨慎谨慎谨慎 这里本来直接翻译的， 因为心急还把+ 错误的翻译成了max(left[1], right[1])
                ans[1] = max(ans[0], left[0]+right[0]+tree.val)
            return ans

        return rob(root)[1]