class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 0:  return 0
        if n <= 3:  return max(nums)

        ans = [[0,0] for _ in range(n)]
        ans[0][1] = nums[0]
        for i in range(1,n): #其实这里只用直接n-1
            ans[i][0] = max(ans[i-1][1],ans[i-1][0])
            ans[i][1] = ans[i-1][0] + nums[i]
        p1 = ans[n-1][0]

        nums, n = nums[1:], n-1
        ans = [[0,0] for _ in range(n)]
        ans[0][1] = nums[0]
        for i in range(1,n):
            ans[i][0] = max(ans[i-1][1],ans[i-1][0]) #@yuzhoujr 这里可以用滚动数组优化 ans[i%2][0] = max(ans[(i-1)%2, ans[(i-1)%2][0]])
            ans[i][1] = ans[i-1][0] + nums[i]

        return max(p1, ans[n-1][1],ans[n-1][0])

    def rob(self, nums) -> int: #我自己的improved_version： 52ms -> 40ms
        n = len(nums)
        if n == 0:  return 0
        if n <= 3:  return max(nums)
        prev, last = 0, nums[0] #其实不用这样， 直接now=prev=0 即可从0开始了 
        for i in range(1, n):
            cur = max(prev + nums[i], last) #@Stefan 这2行可以直接now, prev = max(now, prev+nums[i]), now
            prev, last = last, cur
        p1 = max(prev, last)

        prev, last = 0, nums[1]
        for i in range(2, n):
            cur = max(prev + nums[i], last)
            prev, last = last, cur
        return max(p1, prev, last)

    #Referenced from @Sefan 看看人家的代码 是真的酷
    def rob(self, nums):
        def rob(nums):
            cur = prev = 0
            for num in nums:
                cur, prev = max(prev+num, cur), cur
            return cur
        return max(rob(nums[len(nums) != 1:], rob(nums[:-1])))
    '''p.s. 最酷的nums[len(nums) != 1:]  是用来替代你的if n == 0:  return 0 if n <= 3:  return max(nums) 这2行的
            虽然不建议你在真实的coding中使用 毕竟可读性比较差 但是理解很必要
            这里的并不是针对n=0的情况， 因为它的rob 已经本身safe to conditions when n=0 而且 nums = [] nums[1:]和nums[:-1]都不会报错 且 = 0
            而是针对 n = 1 怕把俩都被排除了。 而这里len(nums)!=1 为True 则从1: 若为False 则刚好从0开始 一举两得 妙妙妙
    '''
