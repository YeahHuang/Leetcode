# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        
        def count(tree: TreeNode) -> int:   #76ms
            tmp_tree = tree
            left_depth = 0
            while tmp_tree!=None:
                tmp_tree = tmp_tree.left
                left_depth += 1
            tmp_tree = tree
            right_depth = 0
            while tmp_tree!=None:
                tmp_tree = tmp_tree.right
                right_depth += 1

                
            if left_depth == right_depth:
                return 2**right_depth - 1
            else:   #这里可以直接 return count(tree.left) + count(tree.right) + 1 84ms
                qpp = count(tree.left)  
                if qpp == 2**right_depth - 1:      
                    return 2**right_depth - 1 + (count(tree.right) - (2**(right_depth-1) - 1)) + 2**(right_depth-1)
                else:
                    return 2**right_depth - 1 + (qpp - (2**(right_depth-1) - 1))

        return count(root)

        '''
        dfs 先判断是否稳定 如果Depth of left most = Depth of right most 就是稳定
        这样可以排除那个最后的节点在哪
        dfs找到最接近的 那个 左右节点不想等的。 然后就可以return了

        计算自己的leftmax 的id 就是整个数的num
        但是需要找一下id的对应关系。 主要是dfs的回传关系咯～。dfs(tree, curIdx, curDepth, totalDepth)
        1. stable 
        2. 传递的本质是关键要反映出最后一行有几个节点 
        '''