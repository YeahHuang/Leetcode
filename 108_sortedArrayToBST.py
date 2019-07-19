class Solution:
    #my own 1st: 72ms
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        if n >= 2:
            idx = n//2 #用mid更好
            tree = TreeNode(nums[idx])       
            tree.left = self.sortedArrayToBST(nums[:idx])
            tree.right = self.sortedArrayToBST(nums[idx+1:])
        elif n == 1:#其实连1的判断都不需要耶
            tree = TreeNode(nums[0])
        else:
            tree = None
        return tree

    #Improved version: 80ms
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:    return None
        mid = len(nums) // 2
        tree = TreeNode(nums[mid])
        tree.left = self.sortedArrayToBST(nums[:mid])
        tree.right = self.sortedArrayToBST(nums[mid+1:]) #[]的左>右只会导致返回空 不会error
        return tree

    #Sol2 用 l, r 来代替nums 据说更优 但我觉得其实空间时间都没啥变化呀 76ms
    def sortedArrayToBST(self, nums):
        # Time: O(n)
        # Space: O(n) in the case of skewed binary tree.
        def convert(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = convert(left, mid - 1)
            node.right = convert(mid + 1, right)
            return node
        return convert(0, len(nums) - 1)