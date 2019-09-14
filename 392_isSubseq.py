class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if set(s).issubset(set(t)) == False: #碰到easy题也要细心吖 不要心急啊 WA一次 一开始这里漏写了
            return False 
        ss, tt = 0, 0
        ls, lt = len(s), len(t)
        while ss<ls and tt<lt:
            while tt<lt and t[tt]!=s[ss]:
                tt += 1
            if tt == lt:
                return False
            ss, tt = ss+1, tt+1
        return ss == ls #easy题也要细心吖 一开始这里直接return True了 至少要好好自己check一下嘛
    
    #Improve： 利用iterator + all 136ms -> 60ms
    def isSubsequence(self, s, t):
        t = iter(t) 
        return all(c in t for c in s)