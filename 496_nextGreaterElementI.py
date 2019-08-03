class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:#56ms faster than 81.4%
        nums2.reverse()
        n = len(nums2)
        ans = {}
        stack = []
        for i in range(n):
            while stack and nums2[i] >= nums2[stack[-1]]:
                stack.pop()
            if stack:
                ans[nums2[i]] = stack[-1]
            else:
                ans[nums2[i]] = -1
            stack.append(i)
        return [ans[num] for num in nums1]

    #看一眼大神的O(mn)解法吧
    def nextGreaterElement(self, findNums, nums):
        return [next((y for y in nums[nums.index(x):] if y > x), -1) for x in findNums]
