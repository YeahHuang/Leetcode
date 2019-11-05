class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
    #本身>=3 num/[1,num-2]
    #本身<=2 num
    
        if len(s)==0:
            return 0
    
        l = [(s[0],1)]
        for i in range(1, len(s)):
            if s[i]==l[-1][0]:
                l[-1] = (l[-1][0], l[-1][1]+1)
                #直接的会tuple object doesnot support item assignment
            else:
                l.append((s[i],1))
        ret = []
        for w in words:
            i = 0
            flag = True
            for (c, cnt) in l: #WA 1 一开始写成了 c cnt in enumerate(l) 了
                #print(c,cnt)
                cnt_w = 0
                while i<len(w) and w[i]==c:
                    cnt_w += 1
                    i+=1    
                if not(cnt==cnt_w or (cnt>=3 and 1<=cnt_w<=cnt)):
                    flag = False
                    break
            if flag:
                ret.append(w)
        print(l,ret)
        return len(ret)
                    
                