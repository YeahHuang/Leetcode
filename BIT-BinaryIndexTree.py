"""
Binary Index Tree树状数组
1. x & (-x) 就是last set bit in a number x
    e.g. 当x=10(decimal) = 1010(b)  x&-x = (10)1(0)&(01)1(0) = 2(decimal)
2. BIT[i] = sum(num[i-(1<<r)+1]..num[i]) r就是上面说的last set bit 
    所以如果i是奇数 就只有它本身; 如果i是2的poweder 那就直接是sum(num[0]..num[i])
3. 需满足可逆性 比如 * / + - 但是gcd这样不可逆的就么的办法了
"""
class BIT:
    def __init__(self, n, nums):
        self.BIT = [0]*(n+1)
        self.n = n 
        for i,num in enumerate(nums):
            self.update(i+1, num)

    def update(self, idx, val):
        while idx <= self.n: 
            self.BIT[idx] += val #add val to current idx and all its' ancestors
            idx += idx & -idx

    def query(self,idx): #或者说queryPrefixSum(idx)
        sum = 0
        while idx>0:
            sum += self.BIT[idx]
            idx -= idx & -idx
        return sum



#Usage
nums = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9] 
bit = BIT(len(nums), nums)
print("Sum of elements in nums[0..5) is %d "% bit.query(5))
nums[3] += 6
bit.update(3, 6)

print("Sum of elements in nums[0..5] after update is %d "% bit.query(5))