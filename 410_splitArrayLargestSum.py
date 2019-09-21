class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        #dfs 可以加记录sum 加一个bar  但是可以带memory  
        #单调增 所以其实你可以看两个的bar 如果在接近&变负了 一定在节点上
        n = len(nums)
        f=[[float('inf')]*m for _ in range(n)]
        f[0][0] = nums[0]
        for i in range(1,n): #n*n*m
            f[i][0] = f[i-1][0] + nums[i]
            last_cut = 0
            for j in range(1, min(i+1,m)):
                
                f[i][j] = max(f[i][0]-f[last_cut][0], f[last_cut][j-1])
                for k in range(last_cut+1, i):
                    if f[i][0]-f[k][0] - f[k][j-1] < 0:
                        if f[k][j-1] < f[i][j]:
                            last_cut = k
                            f[i][j] = f[k][j-1]
                        break
                    elif f[i][0]-f[k][0] < f[i][j]:
                        last_cut = k
                        f[i][j] = f[i][0]-f[k][0]
            
        return f[-1][-1]

    #和1011_capacitytoShipPackagesWithinDDays 有点像的二分dp耶 
    def is_valid(self, nums, m, mid): 
        # assume mid is < max(nums)
        cuts, curr_sum  = 0, 0
        for x in nums:
            curr_sum += x
            if curr_sum > mid:
                cuts, curr_sum = cuts+1, x
        subs = cuts + 1
        return (subs <= m)
    
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        low, high, ans = max(nums), sum(nums), -1
        while low <= high:
            mid = (low+high)//2
            if self.is_valid(nums, m, mid): # can you make at-most m sub-arrays with maximum sum atmost mid 
                ans, high = mid, mid-1
            else:
                low = mid + 1
        return ans