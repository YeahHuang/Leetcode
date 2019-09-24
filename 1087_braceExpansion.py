class Solution:
    #44ms
    def expand(self, S: str) -> List[str]:
        l = -1
        for i, c in enumerate(S):
            if c == '{':
                l = i
                break
        if l == -1:
            return [S]
        for i, c in enumerate(S):
            if c == '}':
                r = i
                break
        tmp = sorted(S[l+1:r].split(','))
        ret1 = self.expand(S[r+1:])
        ret = []
        for c in tmp:
            s0 = S[:l]+c
            for r in ret1:
                ret.append(s0+r)
        return ret

    #48ms
    def expand(self, S):
        A = S.replace('{', ' ').replace('}', ' ').strip().split(' ')
        #当然也可以  lst = S.replace('}','{').split('{')
        B = [sorted(a.split(',')) for a in A]
        return [''.join(c) for c in itertools.product(*B)]

    #更general的方法： 一步步的去看 { } 都会有对应的方法呀 而不是像我那样统一的去看
    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        self.res = []
        def helper(s, word):
            if not s:
                self.res.append(word)
            else:
                if s[0] == "{":
                    i = s.find("}")
                    for letter in s[1:i].split(','):
                        helper(s[i+1:], word+letter)
                else:
                    helper(s[1:], word + s[0])
        helper(S, "")
        self.res.sort()
        return self.res