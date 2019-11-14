class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # strategy: loop through nums, calling it right index.
        # then, find the furthest left index that can be paired with the current right index
        
        # edge cases
        if len(nums) == 0:
            return 0
        if k <= 1:
            return 0
        
        count = left = 0
        prod = 1
        
        # use each index as a right index
        for right, val in enumerate(nums):
            prod *= val
            
            while prod >= k:
                prod /= nums[left]
                left += 1
                
            # once prod is less than k
            count += right - left + 1
            
        return count


class Solution(object):
    
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k<=1:
            return 0
        cnt = 0 
        l = r = 0
        cur_product = 1
        while r<len(nums):
            if nums[r] >= k:
                cnt +=(r-l+1) * (r-l)/2
                l = r = r+1
                cur_product = 1
                continue
            cur_product *= nums[r] 
            if cur_product >= k:
                #cnt += (r-l+1) * (r-l)/2  #(r-1) - l + 1  #starts with l there is already these
                #print(cur_product, l, nums[l], r,cnt)
                while cur_product >= k:
                    cnt += r-l 
                    cur_product /= nums[l]
                    l += 1
            r += 1
        if l != r:
            cnt +=(r-l+1) * (r-l)/2  # (r-l+1 + 1)*(r-l+1) / 2 ~ r-l+1 + r-l + r-l-1 
        print(cur_product, l, r,cnt)    
        '''
        WA 1 in  没有考虑其实k=1 就不会那个了 也没考虑有数组必须考虑是否越界的问题
        [1,1,1]
        1
        WA 2 in  这其实是最初的那个就有了bug
        [10,9,10,4,3,8,3,3,6,2,10,10,9,3]
19
        nums = [10, 5, 2, 6] k = 100
        10 -> 50 -> 100
        l=0, r=3 cnt += 2
        l=1, r=3 cur_product = 10
        10 -> 60 
        cnt += 3+2+1 = (3-1+2)*(3-1+1)/2 = 6 
        
        nums = [1000, 50, 1] k=1000
        l = r = 0 
        '''
        return cnt
        