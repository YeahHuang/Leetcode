class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1 #0 1 2 3 4 5    #5 0 1 2 3 4  #4 5 0 1 2 3
        debug = True
        minimum = nums[0]
        while l < r:
            if nums[l]<nums[r]:
                print("No need to find! break")
                if r<n-1 and nums[r]>nums[r+1]:
                    minimum = nums[r+1]
                break 
            mid = (l+r)//2 #用(l+r)>>2 可以稍微快一点
            if nums[mid]>=nums[mid-1]  and nums[mid]>nums[mid+1]:
                print("already find! mid=%d"%mid)
                minimum = nums[mid+1]
                break
            elif nums[mid] > nums[l]:
                l = mid + 1
            elif nums[mid] == nums[l]:
                while l<mid and nums[l]==nums[mid]:
                    l += 1
                if nums[l]<nums[mid]:
                    minimum = nums[l]
                    break
                else:
                    l += 1
            else:
                r = mid - 1
        if l == r and l<n-1: #一开始没注意[3,1,1]这样的test case 真的测试的时候还是注意考虑全各种case
            minimum = min(minimum, nums[l+1])
        return minimum

        #有人submit里说min(nums) beat了97% 我这里试的时候和我自己的方法一样都是64ms
