class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:  return
        if n <= 2:
            nums.sort()
            return
        i = 1
        while i<n-1:
            if nums[i-1]>=nums[i] and nums[i-1]>=nums[i+1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
            elif nums[i+1]>=nums[i] and nums[i+1]>=nums[i-1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            i += 2
        if n & 1 == 0:
            if nums[n-1]<nums[n-2]:
                nums[n-2], nums[n-1] = nums[n-1], nums[n-2]

        #大神的代码
        for i in range(len(nums)):
            nums[i:i+2] = sorted(nums[i:i+2], reverse = i%2) #这个reverse=i%2也过于酷了一点吧