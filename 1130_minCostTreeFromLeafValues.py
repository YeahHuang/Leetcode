class Solution:
    """
    9:26 - 
    0/2 children 
    non-leaf = max(left_leaf) * max(right_leaf)
    Input: arr = [6,2,4]
    Output: 32
    Explanation:
    There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf  
    node sum 32.

        24            24
       /  \          /  \
      12   4        6    8
     /  \               / \
    6    2             2   4
    数组长度 <= 40 arr[i] <= 15 
    
    dp[l, r] =min(l * max(l+1, r) + dp[l+1,r]) * min(r * max(l, r-1), dp[l, r-1])
    
    dp[i][len] = dp[i+1][len-1]
    
    n*n*n 打表 maxi  dp[i][j] = [maxi(i..cut)  * maxi(cut+1..n) +  dp[i..cut] +   dp[cut+1..j] for cut from i..j-1]
    
    想到实现可能有难度的小跟堆 贪心 每次选择最小的push  & pop   其实还挺类似大佬的做法1了 也是n*n 
    
    bottom-up 的话 max就可以好一些了
    
    10:26

    """
    #sol1 n*n  32ms
    def mctFromLeafValues(self, A):
        res = 0
        while len(A) > 1:
            i = A.index(min(A)) #这个还挺酷的 idx = A.index(target_num)
            res += min(A[i - 1:i] + A[i + 1:i + 2]) * A.pop(i)
        return res


    #我写的 明明理论上O(n)啊 36ms
    def mctFromLeafValues(self, A):
        res = 0
        stack = []
        for num in A:
            while stack and num > stack[-1]: 
                tmp = stack.pop()
                if len(stack) == 0 or stack[-1] > num:
                    res += tmp * num
                else:  #num > stack[-1]
                    res += tmp * stack[-1]
            stack.append(num)

        for i in range(len(stack)-1): #stack is a decreasing list
            res += stack[i] * stack[i+1]
        return res 

    def mctFromLeafValues(self, A):
        res = 0
        stack = [float('inf')]
        for num in A:
            while num >= stack[-1]:
                tmp = stack.pop()
                if stack[-1] > num:
                    res += tmp * num
                else:  #num > stack[-1]
                    res += tmp * stack[-1]
            stack.append(num)

        for i in range(1,len(stack)-1): #stack is a decreasing list
            res += stack[i] * stack[i+1]

        return res 



    #大神的的 24ms
    def mctFromLeafValues(self, A):
        res = 0
        stack = [float('inf')]
        for a in A:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack)  >2:
            res += stack.pop() * stack[-1]
        return res
