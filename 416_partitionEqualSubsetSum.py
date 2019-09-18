class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)&1 == 1:
            return False
        target = sum(nums)//2
        f = set([0])
        for num in nums:
            tmp = set()
            for summ in f:
                if summ + num == target:
                    return True
                if summ + num < target:#WA一次 一开始忘记用tmp 
                    tmp.add(summ+num)
            f = f.union(tmp)
        return False

    def canPartition(self, nums): #480ms -> 200ms 我觉得可以|= 很好
        if sum(nums) & 1 == 0:
            target = sum(nums) >> 1
            cur = {0}
            for i in nums:
                cur |= {i + x for x in cur} 
                if target in cur:
                    return True
        return False

    def canPartition(self, nums): #没办法提前判断target终端了 不是很好
        return (sum(nums) / 2.) in reduce(lambda cur, x: cur | {v + x for v in cur}, nums, {0})