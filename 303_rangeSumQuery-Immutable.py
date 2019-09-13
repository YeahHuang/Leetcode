class NumArray:

    def __init__(self, nums: List[int]):
        self.summ = [0] * (len(nums)+1) #WA一次 写成了self.summ=[0] 而下面的也没写成append
        for i, num in enumerate(nums):
            self.summ[i+1] = self.summ[i] + num

    def sumRange(self, i: int, j: int) -> int:
        return self.summ[j+1] - self.summ[i]
