import collections
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        _, max_times = cnt.most_common(1)[0]
        minimum = len(nums)
        debug = True
        for key, times in cnt.most_common(): #一开始没有考虑到
            if times < max_times:
                break
            for i, num in enumerate(nums):
                if num == key:
                    l = i
                    break
            for i in range(len(nums)-1,-1,-1):
                if nums[i] == key:
                    r = i
                    break
            minimum = min(r-l+1, minimum)
            if debug:
                print(key, times, l, r, minimum)
        return minimum

    def findShortestSubArray(self, nums: List[int]) -> int: #2660ms -> 284ms
        degree = 1
        cnt, left = {}, {}
        minimum = len(nums)
        for i, num in enumerate(nums):
            if num not in left: 
                left[num] = i
            cnt[num] = cnt.get(num,0) + 1 #这个用法学习一下～～
            if cnt[num] > degree:
                degree = cnt[num]
                minimum = i - left[num] + 1
            elif cnt[num] == degree:
                minimum = min(minimum, i - left[num] + 1)
        return minimum