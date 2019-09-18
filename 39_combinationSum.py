class Solution: #time beats 96% 空间用dfs可以优化
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        f = [[] for _ in range(target+1)]
        f[0].append([]) #这2行可以直接写成 f = [[]] + [[] for _ in range(target)]
        for num in candidates:
            for i in range(num, target+1):
                for l in f[i-num]:
                    f[i].append(l+[num])
        '''
        一开始写的for 的顺序反了就会 WA 出现 [2,3,2] [2,2,3] [3,2,2] 判重还特别慢 换一下思路就OK啦
        for i in range(1, target+1):
            for num in candidates:
                if i>num:
                    for l in f[i-num]:
                        f[i].append(l+[num])
            for l in f[i]:
                l.sort()
            f[i] = list(set(f[i]))
        '''      
        
        return f[-1]