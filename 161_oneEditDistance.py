class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        for i in range(min(len(s), len(t))):
            if s[i]!=t[i]:
                return s[i:]==t[i+1:] or s[i+1:]==t[i:] or s[i+1:]==t[i+1:]
        #one is ""; all equals; previous no equals
        return abs(len(s)-len(t)) == 1

        '''直接把72的搬过来会TLE
        f = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)): #一开始忘记初始化了 这4行以后要留意吖
            f[i+1][0] = i+1
        for j in range(len(word2)):
            f[0][j+1] = j+1
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    f[i+1][j+1] = f[i][j]
                else:
                    f[i+1][j+1] = min(f[i][j], f[i+1][j], f[i][j+1]) + 1
        return f[-1][-1]==1
        '''