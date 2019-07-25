class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 0:  return 0
        ans = [[0,0] for _ in range(n)]
        ans[0][1] = nums[0]
        for i in range(1,n):
            ans[i][0] = max(ans[i-1][1],ans[i-1][0])
            ans[i][1] = ans[i-1][0] + nums[i]
        return max(p1, ans[n-1][1],ans[n-1][0])
        

    #优化的话就是因为其实只需要记录取的情况即可 优化后40ms -> 32ms
    def rob(self, nums): 
        n = len(nums)
        if n == 0:  return 0
        if n == 1:  return nums[0]
        ans = [0] * n
        ans[0], ans[1] = nums[0], max(nums[0],nums[1])
        for i in range(2, n):
            ans[i] = max(ans[i-2]+nums[i], ans[i-1])
        return ans[n-1]