class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #Solution 1 时间O(n*n) 空间O(n) TLE
        if nums==[]:
            return 0
        sums = [0]
        n = len(nums)
        for i in range(n):
            sums.append(sums[-1]+nums[i])
        cnt = 0
        for i in range(n+1):
            for j in range(i+1,n+1): #WA一次 在k=0 因为j从i开始 
                                    #我也不知道为什么我明明想到了这个case 但是还是写错了 以后要记得验证呀
                if sums[j]-sums[i] == k:
                    cnt += 1
        return cnt

    def subarraySum(self, nums: List[int], k: int) -> int:
        #Solution2 时间O(n*n) 空间O(n) TLE  其实和Sol1 几乎一模一样 但简短可爱一点
        n = len(nums)
        cnt = 0
        for i in range(n):
            sum_i = 0
            for j in range(i,n):
                sum_i += nums[j]
                if sum_i == k:
                    cnt += 1
        return cnt

    def subarraySum(self, nums, k): #Sol 3 O(n) 空间很大 56ms
        hash_sum = {0: 1}
        tmp_sum = 0
        cnt = 0 #我发现cnt是我经常referened before used 的一个变量
        for num in nums:
            tmp_sum += num
            if tmp_sum - k in hash_sum.keys():
                cnt += hash_sum[tmp_sum-k]
            if tmp_sum in hash_sum.keys():
                hash_sum[tmp_sum] += 1
            else:   #一开始竟然忘记写else了
                hash_sum[tmp_sum] = 1
            
        return cnt