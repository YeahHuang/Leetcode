class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l<=r: #出现重复的时候主要是如果 nums[mid]==nums[l]==nums[r] 1 1 3 1 1 1 1 1 怎么办呢？
            mid = (l+r)//2
            if nums[mid]==target:
                l = mid
                break
            while l<mid and nums[l] == nums[mid]:
                l += 1
            if nums[l] == target:
                break
            #if nums[l]<=target<nums[mid] or target >= nums[l]> nums[mid] or nums[l]>nums[mid]>target: 
            #用xor的方法 可以从84ms -> 52ms 
            if (nums[l]>target) ^ (nums[l]>nums[mid]) ^ (target > nums[mid]): 
                #可以用 if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]): xor代替
                #一开始WA是因为 没有判断nums[l]=target的情况 
                l = mid + 1
                #r = mid - 1
            else:
                r = mid - 1
                #l = mid + 1
            
        return l<len(nums) and nums[l]==target