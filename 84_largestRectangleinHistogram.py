class Solution:
    #Sol1 TLE(对单调增序列相当于0优化) 
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxi = 0
        stack = []  
        for i, h in enumerate(heights):
            last_i = i  # WA1 in [2,1,2] 忘记加last_i 
            while stack and stack[-1][1]>h:
                last_i, last_h = stack.pop()
            if stack==[] or stack[-1][1] < h:
                stack.append((last_i, h))
            maxi = max(maxi, max(map(lambda x: (i-x[0]+1)*x[1], stack))) #这个map写出来还挺酷的嘿嘿
        return maxi

    #Sol1.1 128ms 其实你已经非常接近正确答案了啊！ 就是pop的位置稍微有点问题 其实只需要pop的时候去计算就OK啦
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxi = 0
        heights.append(0)
        stack = []  
        for i, h in enumerate(heights):
            last_i = i  # WA1 in [2,1,2] 忘记加last_i 
            while stack and stack[-1][1]>h:
                last_i, last_h = stack.pop()
                maxi = max(maxi, (i-last_i)*last_h)
            if stack==[] or stack[-1][1] < h:
                stack.append((last_i, h))
        return maxi

    #Sol2 176ms 又花了30min 写了下面那个Improved version faster than 5%  156ms
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxi, n = 0, len(heights)
        if n==0:    return 0
        stack = [(0,heights[0])]
        f = [[1]*2 for _ in range(n)]
        for i in range(1, n): #精良后
            if heights[i]>heights[i-1]:
                stack.append((i, heights[i]))
                f[i][0] = 1
            elif heights[i] == heights[i-1]:
                f[i][0] = f[i-1][0] + 1
            else:
                while stack and stack[-1][1]>=heights[i]:
                    last_i, _ = stack.pop()
                stack.append((last_i, heights[i]))
                f[i][0] = i - last_i + 1
        
        #Improved 2.2 上面那个可以简略成下面的这几行 if elif else 都可以被精炼的
        '''
        for i in range(1, n):
            last_i = i
            while stack and stack[-1][1]>=heights[i]:
                last_i, _ = stack.pop()
            stack.append((last_i, heights[i]))
            f[i][0] = i - last_i + 1
        '''
        stack = [(n-1,heights[-1])]
        maxi = f[-1][0] * heights[-1]
        for i in range(n-2, -1, -1):
            if heights[i]>heights[i+1]:
                stack.append((i, heights[i]))
                f[i][1] = 1
            elif heights[i] == heights[i+1]:
                f[i][1] = f[i+1][1] + 1
            else:
                while stack and stack[-1][1]>=heights[i]:
                    last_i, _ = stack.pop()
                stack.append((last_i, heights[i]))
                f[i][1] = last_i-i + 1
            maxi = max(maxi, heights[i] * (f[i][0]+f[i][1]-1))
        return maxi

    