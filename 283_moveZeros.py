class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Sol 1  48ms
        zero_num = 0 
        i = 0
        while i < len(nums): #一开始写成了i<len(nums)-zero_num 但忽略了你并没有真实的pop吖
            while i < len(nums)  and nums[i]!=0:
                nums[i-zero_num] = nums[i]
                i += 1 
            while i < len(nums) and nums[i]==0:
                zero_num += 1
                i += 1
        for i in range(len(nums)-1,  len(nums)-zero_num-1, -1):
            nums[i] = 0

        #Sol 2  48ms
        i = 0
        end = len(nums)
        while i < end:
            if nums[i] == 0:
                del nums[i] #或者nums.pop(i) nums.remove(i)
                nums.append(0)
                end -= 1
            else:
                i += 1

        #Sol 3      40ms
        count = nums.count(0)
        nums[:] = [i for i in nums if i!=0] #如果这里写成 if i 就会变成60ms的时间 神奇
        nums += [0]*count
