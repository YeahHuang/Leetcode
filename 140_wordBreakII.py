import copy 
class Solution:
    def wordBreak(self, s: str, wordDict):
        #总结了MLE后 还是会TLE
        if s == "" or len(wordDict)==0: #一开始只考虑了一个s为空 WA了1次 
            return [] 
        wordDict.sort(key = lambda x: len(x))
        length = []
        words = []
        length.append(len(wordDict[0])) #写出这个的时候就需要考虑security了
        words.append([wordDict[0]])
        debug = True
        
        for word in wordDict[1:]:
            if len(word) == length[-1]:
                words[-1].append(word)
            else:
                length.append(len(word))
                words.append([word])
        if debug:
            for i in range(len(length)):
                print("For length=",length[i], words[i])
        
        #MLE
        ans = {} 
        #ans = [[] for _ in range(len(s))]
        for i in range(len(s)):
            ans[i] = []
            for j in range(len(length)):
                if length[j]>i+1:
                    break
                if length[j]==i+1: 
                #优化： 节省空间 可以记录father[i]
                #还有一种是其实只需要记录 maxLength长度
                    if s[:i+1] in words[j]:
                        ans[i].append(s[:i+1])
                else:
                    if (i-length[j]) in ans and s[i-length[j]+1:i+1] in words[j]:
                        for ans_str in ans[i-length[j]]: 
                            ans[i].append(ans_str+' '+s[i-length[j]+1:i+1])#WA1 输出格式错误
            if len(ans[i])==0:
                del ans[i]
        return ans[len(s)-1]
    
        max_word_length = len(wordDict[-1])
        pre = [[] for _ in range(max_word_length+1)] #其实最后一位还是用不上
        pre[0].append("")
        start_idx = 0
        #[i] should indicate answers till i(not including i)  
        #法1 用一个arr试一试  法2 分步判断 
        #所以end with i 的ans 存于 [i+1]
        while start_idx<len(s):
            if debug:
                print(start_idx,":", pre)
            cur = [[] for _ in range(max_word_length+1)]
            for i in range(start_idx, min(start_idx+max_word_length, len(s))):
                for j in range(len(length)):
                    if length[j]>=i-start_idx+1: 
                        #if i==6:
                        #    print(length[j],  pre[(i+1-length[j])%max_word_length],  s[i-length[j]+1:i+1])
                        if len(pre[(i+1-length[j])%max_word_length])>0 and s[i-length[j]+1:i+1] in words[j]:
                            for ans_str in pre[(i+1-length[j])%max_word_length]:
                                if ans_str!="":
                                    cur[(i+1)%max_word_length].append(ans_str+' '+s[i-length[j]+1:i+1])#WA1 输出格式错误
                                else:
                                    cur[(i+1)%max_word_length].append(s[start_idx:i+1])
                    else:
                        if len(cur[(i+1-length[j])%max_word_length])>0 and s[i-length[j]+1:i+1] in words[j]:
                            for ans_str in cur[(i+1-length[j])%max_word_length]:
                                if ans_str!="":
                                    cur[(i+1)%max_word_length].append(ans_str+' '+s[i-length[j]+1:i+1])#WA1 输出格式错误
                                else:
                                    cur[(i+1)%max_word_length].append(s[start_idx:i+1])
                if debug:
                    print(cur[(i+1)%max_word_length]) 
            start_idx += max_word_length
            pre = copy.deepcopy(cur)         
        return cur[(len(s)-1+1)%max_word_length]

    #MD 我真的觉得我MLE的那个方法和这个完全一样吖 而且还和网上那些加了优化的该法子特别像 为什么它的就不会MLE 哭哭.jpg
    def wordBreak_dfs_Mem(self, s, wordDict):
        momo = {len(s): ['']}
        def setences(i):
            if i not in memo:   #"and" returns the first null value, or the last non-null value
                memo[i] = [s[i:j] + (tail and ' '+tail) #所以这里and意思就是如果tail是空‘’ and的结果就是空 其他都是加一个空格
                for j in range(i+1, len(s)+1)
                if s[i:j] in wordDict
                for tail in sentences(j)]
            return memo[i]
        return sentences(0)

    #Improved One: 和我一样统计了一下长度
    def wordBreak(self, s, wordDict):
        memo = {len(s): ['']}
        ss = set(len(x) for x in wordDict)
        def sentences(i):
            if i not in memo:
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                           for j in [i + x for x in ss]
                           if s[i:j] in wordDict
                           for tail in sentences(j)]
            return memo[i]
        return sentences(0)
        
sol = Solution()
'''
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
'''
s="pineapplepenapple"
wordDict=["apple","pen","applepen","pine","pineapple"]
print(sol.wordBreak(s, wordDict))