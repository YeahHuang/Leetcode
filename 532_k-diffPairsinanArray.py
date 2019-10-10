class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt = 0
        if k<0:#WA1 没考虑 k<0 因为没有认真读题目中的abs部分说明
            return 0
        if k == 0:  #WA2 一开始没考虑 k = 0 
            tmp = set()
            counted = set()
            for num in nums:
                if num in tmp and num not in counted:
                    cnt += 1
                    counted.add(num)
                tmp.add(num)
        else:
            nums = list(set(nums))
            tmp = set() #这个其实根本不用 你直接判断 num + k in nums 即可 num - k 也不用
            for num in nums:
                if num + k in tmp:
                    cnt += 1
                if num - k in tmp:
                    cnt += 1
                tmp.add(num)
        return cnt

    def findPairs(self, nums, k):
        if k>0:
            #return len(set(nums)&set(n+k for n in nums)) #所以可以进一步优化成nums 和 num + k集合的并
            return len(set(nums) & {n+k for n in nums}) #根据@stephan的想法 {}会比⬆️的set()更快 
        elif k==0:
            sum(v>1 for v in collections.Counter(nums).values())
        else:
            return 0
    
class Solution:
    def findPairs(self, nums, k):
        res = 0
        c = collections.Counter(nums)
        for i in c:
            if k > 0 and i + k in c or k == 0 and c[i] > 1:
                res += 1
        return res


'''
@Stephan大神的测试
>>> from timeit import timeit
>>> timeit('set(n+k for n in nums)', 'nums, k = range(10000), 10000', number=10000)
6.103899186630329
>>> timeit('{n+k for n in nums}',    'nums, k = range(10000), 10000', number=10000)
4.561420978146888
'''