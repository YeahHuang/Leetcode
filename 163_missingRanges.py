class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums.sort()
        nums.insert(0, lower-1)
        nums.insert(len(nums),upper+1)
        ret = []
        for i in range(len(nums)-1):
            if nums[i]+1 < nums[i+1]:
                if nums[i]+2 == nums[i+1]:
                    ret.append(str(nums[i]+1))
                else:
                    ret.append(str(nums[i]+1) + '->' + str(nums[i+1]-1))
        return ret