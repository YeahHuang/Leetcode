class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        #Sol1 sort & find cur_num faster than 90%
        NUM,ans = 80000,0
        A.sort()
        cur_num = -1
        for i, num in enumerate(A):
            if num <= cur_num:
                cur_num += 1
                ans += cur_num - num
                
            else:
                cur_num = num
        return ans
        
        '''
        Sol2 hashmap TLE
        m = [False] * NUM
        for num in A:
            for j in range(num, NUM):
                if m[j]==False:
                    m[j] = True
                    ans += j - num
                    break
        '''
        
        return ans
