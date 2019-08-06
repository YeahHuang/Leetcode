class Solution:

    #Sol1 Ori O(n) 其实你已经很接近 dp 只是其实不需要把ups&downs全部去掉 不然这样的边界条件加上去就显得代码很冗余
    def maxSubArray(self, nums: List[int]) -> int: #88ms
        i, n = 1, len(nums)
        if n==0:    return 0
        if n==1:    return nums[0]
        if max(nums)<=0:    return max(nums)
        while i<n:
            if nums[i-1]*nums[i]>=0:
                nums[i-1] += nums[i]
                nums.pop(i)
                n-=1
            else:
                i+=1
        if n==1:
            return nums[0]
        if nums[-1]<=0:
            nums.pop()
        if nums[0]<=0:
            nums.pop(0)
        i = len(nums)-1
        max_sum = 0    
        while i >= 2:
            max_sum = max(max_sum, nums[i])
            if nums[i]+nums[i-1]>0:
                nums[i-2] += nums[i-1]+nums[i]
            i -= 2
        max_sum = max(max_sum, nums[0])
        return max_sum

    #Sol2 简介版 88ms -> 80ms
    def maxSubArray(self, nums: List[int]) -> int: 
        n = len(nums)
        dp = [0] * n #dp[idx] 表示以idx为结尾的subarray 最大和可以是多少
        max_sum = dp[0] = nums[0]
        for i in range(1,n):
            dp[i] = max(dp[i-1],0) + nums[i]
            max_sum = max(max_sum, dp[i])
        return max_sum