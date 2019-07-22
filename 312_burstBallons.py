class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        def dfs(left, right) -> int:
            if max_coins[left][right]!=-1:
                return max_coins[left][right]
            '''
            if right-left == 2:
                max_coins[left][right] = nums[left]*nums[left+1]*nums[right]
                return max_coins[left][right]
            '''

            #差了一个到着爆炸的想法 其实已经写到这里了耶 真的就差一点点 卡在了不知道第一个爆炸怎么穿题的问题
            max_coins[left][right] = max(nums[left]*nums[i]*nums[right] + dfs(left,i) + dfs(i,right) for i in range(left+1, right))
            return max_coins[left][right]

        nums.insert(0,1) #可以写成 nums = [1] + nums + [1]
        nums.append(1)
        max_coins = [[-1 for j in range(len(nums))] for i in range(len(nums))]
        #可以写成max_coins = [ [0]*n for _ in range(n)]
        for i in range(len(max_coins)-1):
            max_coins[i][i+1] = 0 
        dfs(0, len(nums)-1)

        return max_coins[0][len(nums)-1]


        #Sol1.1 不dfs版本 748ms -> 304ms
        nums = [1] + nums + [1]
        n = len(nums)
        max_coins = [[0] * n for _ in range(n)]
        for left in range(n-3, -1, -1):
            for right in range(left+2, n):
                max_coins[left][right] =  max(nums[left]*nums[i]*nums[right] + max_coins[left][i] + max_coins[i][right] for i in range(left+1, right))
        return max_coins[0][n-1]