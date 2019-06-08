class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:



        S_without_dash = ""
        for c in S:
            if c!='-':
                S_without_dash += c #这里果断得能用S.replace("-","") 不然过愚蠢了
        print(S_without_dash)
        N = len(S_without_dash)
        S_formatted = ""
        for c in S_without_dash[:N%K]:
            S_formatted += c.upper()。#一开始还自己写了transfer函数 明明自带.upper
        idx = N%K
        while idx<N:
            if len(S_formatted):
                S_formatted += '-'
            for c in S_without_dash[idx: idx+K]:  #其实可以直接join
                S_formatted += c.upper()
            idx += K
        return S_formatted

        '''
        以下是大神的code： ym ym ym
        S = S.replace("-", "").upper()[::-1]
        return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]. 
        '''

        '''
        以下是大神的code： ym ym ym
        S = S.replace("-", "").upper()[::-1]
        return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]
        #