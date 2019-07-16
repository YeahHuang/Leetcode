# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    #Sol1: 排序后check 是否sorted
    def isValidBST(self, root: TreeNode) -> bool:  
        def BST2list(tree:TreeNode) -> list: #transfer tree to list 这个其实是有python自带的
            if tree == None:
                return []
            return BST2list(tree.left) + [tree.val] + BST2list(tree.right)

        BST_list = BST2list(root)

        #Sol1.1 72ms
        return BST_list == sorted(list(set(BST_list))) 
        #WA一次 因为一开始错误的写成了list(set(sorted(BST_list))) 先sort 再set 那sort都没意义了吖

        #可以用⬆️一行 或者接下来这一段判断
        #Sol1.2 56ms   没想到还是我这个ori的最快耶 
        flag = True
        for i in range(1,len(BST_list)): 
            if BST_list[i]<BST_list[i-1]:
                flag = false
                break
        return flag

    #Sol2: 更传统的比较 60ms     
    def isValidBST(self, root, floor = float('-inf'), ceiling = float('inf')):
        if not root:
            return True
        if root.val <= floor or root.val >= ceiling:
            return False
        return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)