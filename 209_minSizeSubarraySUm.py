class Solution:

    #Sol1 Binary Search O(NlogN) 100ms
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        summ = [0] * (len(nums)+1)
        for i in range(len(nums)):
            summ[i+1] = summ[i] + nums[i]
        if summ[len(nums)] < s:
            return 0
        min_len = float('inf')
        for i in range(len(nums)):
            if summ[i]+s<=summ[-1]: #WA一次 找不到的话 bisect_left 是直接定义在list末尾的
                min_len = min(min_len, bisect.bisect_left(summ, summ[i]+s) - i) #WA一次 用了bisect.bisect_right
        return min_len

    #Sol2 two pointers O(n) 80ms
    def minSubArrayLen(self, s: int, nums: List[int]) -> int
        summ = 0
        min_len = len(nums) + 1
        start_idx = 0
        for i in range(len(nums)):
            summ += nums[i]
            if summ >= s:
                min_len = min(min_len, i - start_idx + 1) #一开始没考虑到这里
                summ -= nums[start_idx]
                start_idx += 1
        return min_len if min_len!=len(nums)+1 else 0