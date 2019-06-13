class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        idx = -1 
        if len(nums):
            idx = 0 
            for i in range(1, len(nums)):
                if nums[i] != nums[idx]:
                    idx += 1
                    nums[idx] = nums[i]
        return idx+1

        像 nums = list(set(nums))
        nums =[k for k, v in itertools.groupby(nums)]
        因为没有remove最后的元素  都是不可行的
        '''
        
        if not nums:   #如果list是空的 直接返回 不然之后idx+1 会越界 WA
            return 0
        idx = 0        #如果list不空 那么第一个元素 肯定不会被删 所以初始化idx(index的缩写)为0
                       #idx 表示的是不重复的nums的当前位置 
        debug = True
        for i in range(1, len(nums)):  
            if nums[i] != nums[idx]:  #如果nums[i]和nums[idx]不同
                idx += 1              #证明 又多了个不重复的元素
                nums[idx] = nums[i]   #赋值
            if debug:
                print("i=",i, "nums:",nums)
        return idx + 1                #因为list编号从0开始 所以实际长度+1