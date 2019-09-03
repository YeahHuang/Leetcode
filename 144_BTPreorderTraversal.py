class Solution:
    
    #Sol1 recursive 36ms
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        else:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    
    
    
    #Sol2 iterative 40ms
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        ret = []
        while True:
            if not stack:
                break
            tmp_node = stack.pop()
            if tmp_node is not None:
                ret.append(tmp_node.val)
                stack.append(tmp_node.right)
                stack.append(tmp_node.left)
        return ret