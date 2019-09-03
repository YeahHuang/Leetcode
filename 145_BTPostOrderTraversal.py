class Solution:
    
    #Sol1 recursive 40ms
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        else:
            return  self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
    
    
    #Sol2 iterative 我的 加了一个type 32ms
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        #(TreeNode/int, Bool-whether it is TreeNode)
        stack = [(root, True)]
        ret = []
        while True:
            if not stack:
                break
            tmp_node, isTreeNode = stack.pop()
            if tmp_node is not None:
                if isTreeNode:
                    stack.append((tmp_node.val,False))
                    stack.append((tmp_node.right, True))
                    stack.append((tmp_node.left, True))
                else:
                    ret.append(tmp_node)
        return ret
    
    #Sol3 iterative 用倒置数组来解决后序的问题 36ms
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        ret = []
        while True:
            if not stack:
                break
            tmp_node = stack.pop()
            if tmp_node is not None:
                ret.append(tmp_node.val)
                stack.append(tmp_node.left)
                stack.append(tmp_node.right)
        return ret[::-1]
    
    