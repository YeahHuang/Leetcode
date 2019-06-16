class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        #Sol1 set   发现list化的sum会更快哟
        return 2 * sum(list(set(nums))) - sum(nums) #32ms 14.8M
        return 2 * sum(set(nums)) - sum(nums) # 56ms 15M
        
        #Sol2 xor    36ms 14.6M
        qpp = 0     
        for i in nums:
            qpp ^= i
        return qpp
        
        '''
        #Sol3 哈希    64ms 15.3M
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1 
        return hash_table.popitem()[0] #唯一一个没被pop的就是single
      
        