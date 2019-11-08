class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0
        cnt = 1 if len(nums) else 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
        ans = max(ans, cnt)
        return ans