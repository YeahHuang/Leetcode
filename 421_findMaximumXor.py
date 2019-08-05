class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        '''
        每一个数push进对应的32的list 每到空的那一位 把所有的int push进一个list
        一个个的对照 去看 哪一个被miss 
        每一个在分析完后可以立刻得到自己的miss point list？
       
        O 
        '''
        max_xor, n = 0, len(nums)  # O(n*n) TLE
        for i in range(n):
            for j in range(i+1,n):
                max_xor = max(max_xor, nums[i]^nums[j])
        return max_xor

        max_xor, n = 0, len(nums) # max的话也可以到O(n*n) 我在想是可以利用absent搞一下 但是 嗯 有待考证吧～ 打算先叉出去做一下Trie看看
        xor = [[] for _ in range(31)]
        absent = [[] for _ in range(n)]
        for i,num in enumerate(nums):
            for j, c in enumerate(bin(num)[2:][::-1]):
                if c=='1':
                    xor[j].append(i)
                else:
                    absent[i].append(j)
        max_idx = 0 #RE了一次 因为没加这个 如果nums=[]  会 referenced before assignment
        for j in range(30,-1,-1):
            if len(xor[j])>0:
                max_idx = j
                break
        for i in xor[max_idx]:
            for j in range(n):
                max_xor = max(max_xor, nums[i]^nums[j])
        return max_xor

