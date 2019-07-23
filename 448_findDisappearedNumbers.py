class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #hashmap set  xor 
        nums = set(nums)
        #其实直接set判定就行 但可能算是用了额外空间？
        ans = []
        for i in range(1,n+1): 
            if i not in nums:
                ans.append(i)
        return ans


        #别人的 Sol2 可以对比我的⬇️
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = - abs(nums[idx])
        return [i + 1 for i in range(len(nums)) if nums[i]>0]  #用这个代替我的最后3行 就很酷 


        '''
        #WA的sol 其实和标准的很像了 但我的就是直接和自己位置的swap一下 但是存在前面的值给置换了的问题 就会WA
        for i, num in enumerate(nums):
            if num != i+1:
                nums[num-1], nums[i] = nums[i], nums[num-1]
        ans = []
        for i, num in enumerate(nums):
            if num != i+1:
                ans.append(i+1) 
        return ans
        '''