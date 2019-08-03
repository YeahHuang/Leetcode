class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        T.reverse()
        n = len(T)
        ans = [0] * n
        pos = [-1] * 101
        pos[T[0]] = 0
        for i in range(1,n):
            nearest_idx = -1
            for temp in range(T[i]+1,  101):
                if pos[temp]!=-1:
                    nearest_idx = max(nearest_idx, pos[temp])
            if nearest_idx!=-1:
                ans[i] = i - nearest_idx
            pos[T[i]] = i
        return reversed(ans)

    #优化方案：倒序的时候那些比前面大 还 近的自然会被pop掉
    def dailyTemperatures(self, T: List[int]) -> List[int]: #1280ms -> 556ms
        T.reverse()
        n = len(T)
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = i - stack[-1]
            stack.append(i)
        return reversed(ans)
