class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_pos = [0]*n
        dp_neg = [0]*n
        if n == 0: return 0
        if nums[0]>0:
            dp_pos[0] = nums[0]
        else:
            dp_neg[0] = nums[0]
        for i, num in enumerate(nums):
            if num > 0: #优化点在于 其实不用判断符号 直接一股脑max min得了
                if dp_pos[i-1] > 0:
                    dp_pos[i] = num * dp_pos[i-1]
                else:
                    dp_pos[i] = num
                if dp_neg[i-1] < 0:
                    dp_neg[i] = num * dp_pos[i-1]
            else:
                if dp_neg[i-1] < 0:
                    dp_pos[i] = num * dp_neg[i-1]
                if dp_pos[i-1] > 0:
                    dp_neg[i] = num * dp_pos[i-1]
                else:
                    dp_neg[i] = num 
        return max(dp_pos+dp_neg) #其实只要n>1 是不用管dp_neg

    def maxProduct(nums):
        maximum = big = small = nums[0]
        for num in nums[1:]:
            big, small = max(num, num*big, num*small), min(num, num*big, num*small)
            maximum = max(maximum, big)
        return maximum