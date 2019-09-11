# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int, cur_sum=[0]) -> int:
        ''' 248ms
        1. transfer the root to a list
        2. dfs to traverse its cur_idx, cur_sum, cur_path  return valid path 
        3. returns end with cur_idx, what is the sum   
        ''' 
        if root is None: #WA一次 一开始没考虑到这个空会root.val无法引用而报错
            return 0
        cur_sum.append(cur_sum[-1]+root.val)
        ret = 0
        if root.left is not None:
            ret += self.pathSum(root.left, sum, cur_sum)
        if root.right is not None:
            ret += self.pathSum(root.right, sum, cur_sum)
        for i in range(len(cur_sum)-1):
            ret += (cur_sum[-1] - cur_sum[i])==sum #把这里从cur_sum[len(cur_sum)-1]改为cur_sum[-1] 340ms -> 248ms
        cur_sum.pop()
        return ret

#Improve2 增加cur_sum_dict 代替原来的遍历查找 空间 15->15.5 时间248ms -> 56ms 棒！
class Solution:
    def pathSum(self, root: TreeNode, sum: int, cur_sum=[0], cur_sum_dict = {0:1}) -> int:
        if root is None: #WA一次 一开始没考虑到这个空会root.val无法引用而报错
            return 0
        ret = 0
        cur_sum.append(cur_sum[-1]+root.val)
        if cur_sum_dict.get(cur_sum[-1] - sum) is not None:
            ret += cur_sum_dict.get(cur_sum[-1] - sum)
        if cur_sum_dict.get(cur_sum[-1]) is None:
            cur_sum_dict[cur_sum[-1]] = 1
        else:
            cur_sum_dict[cur_sum[-1]] += 1
        
        '''
        这里不用多判断 转化成下面的1行 快了4ms
        if root.left is not None:
            ret += self.pathSum(root.left, sum, cur_sum)
        if root.right is not None:
            ret += self.pathSum(root.right, sum, cur_sum)
        '''
        ret += self.pathSum(root.left, sum, cur_sum) +  self.pathSum(root.right, sum, cur_sum)
        
        '''
        这里不用4行 转化成上面的两行 可以对sum==0 减少一层判断 快了4ms
        for i in range(len(cur_sum)-1):
           ret += (cur_sum[-1] - cur_sum[i])==sum
        if sum == 0:
            ret -= 1
        '''
        cur_sum_dict[cur_sum[-1]] -= 1
        cur_sum.pop()
        return ret
        

        