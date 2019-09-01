class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #最简单的自然是开一个新的list 长度相同 所以可以从前到后的覆盖 
        #其次就是写pre_left, pre_right, rev_left, rev_right 每个都记录一下当前的单词 避免被覆盖 
        right_insert_idx, tmp_left, tmp_right = 0, [], []
        pre_left, rev_left, pre_right, rev_right = 0, 0, len(s)-1, len(s)-1
        debug = False
        if ' ' not in s:
            return
        while pre_left < pre_right:
            if tmp_left==[]:#pre_left==rev_left:
                while pre_left < len(s) and s[pre_left]!=' ': 
                    tmp_left.append(s[pre_left])
                    pre_left+=1
                tmp_left.append(' ')
                pre_left += 1
            if tmp_right==[]:
                right_insert_idx = len(tmp_right)
                while pre_right >= 0 and s[pre_right]!=' ':
                    tmp_right.insert(right_insert_idx, s[pre_right])
                    pre_right-=1
                tmp_right.append(' ')
                pre_right -= 1
            if pre_left - rev_left >= len(tmp_right): #还没考虑空格 + 刚好等于的情况
                s[rev_left: rev_left+len(tmp_right)] = tmp_right
                rev_left, tmp_right = rev_left+len(tmp_right), []
            if rev_left<rev_right and rev_right - pre_right >= len(tmp_left):
                if rev_right == len(s)-1:
                    tmp_left = tmp_left[:-1]
                s[rev_right+1-len(tmp_left) :rev_right+1] = tmp_left
                rev_right, tmp_left = rev_right-len(tmp_left), []
            if debug:
                print(tmp_left, tmp_right, pre_left, rev_left, pre_right, rev_right, s)
        if tmp_left!=[]:
            if rev_right == len(s)-1:
                tmp_left = tmp_left[:-1]
            s[rev_right+1-len(tmp_left) :rev_right+1] = tmp_left

        if tmp_right!=[]:
            s[rev_left: rev_left+len(tmp_right)] = tmp_right
            
            '''
            if len(tmp_left) == len(tmp_right):
                
                
                s[pre_right+1: pre_right+1+len(tmp_right)] = tmp_left
                s[pre_left-len(tmp_left) : pre_left] = tmp_right
                pre_left += 1
                pre_right -= 1
                tmp_left, tmp_right, right_insert_idx = [], [], 0 
                
            elif len(tmp_left) > len(tmp_right):  #增大right 
                s[pre_left-len(tmp_left): pre_left-len(tmp_left)+len(tmp_right)] = tmp_right
                tmp_right, right_insert_idx = [], 0 
            else:
                s[pre_right+1+len(tmp_right)-len(tmp_left) :pre_right+1+len(tmp_right)] = tmp_left
                tmp_left, right_insert_idx = [], len(tmp_right)
            '''
    #Sol2(more concise): 1st - reverse the whole string.  2nd - reverse word by word
    #时间都是304ms
    def reverseWords(self, s: List[str]) -> None:
        s.reverse()
        start_idx = 0 
        for i in range(len(s)):
            if s[i] == ' ':
                s[start_idx: i] = reversed(s[start_idx: i])  #s[start_idx:i][::-1]的话是308ms
                start_idx = i + 1
            elif i == len(s) - 1:
                s[start_idx: i+1] = reversed(s[start_idx: i+1]) 

