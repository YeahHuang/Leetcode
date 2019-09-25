class Solution:
    def zip(self,list1, list2):
        ret = []
        if list1==[] or list2==[]:
            return list1 if list2==[] else list2
        for s1 in list1:
            for s2 in list2:
                ret.append(s1+s2)
        return ret

    def braceExpansionII(self, expression: str) :
        debug = True
        if ('{' not in expression) and (',' not in expression):
            return [expression]
        if expression[0]!='{':
            for i, c in enumerate(expression):
                if c == '{':
                    return [expression[:i]+s for s in self.braceExpansionII(expression[i:])]
            return [expression]
        brace_no = 0
        ret = set()
        last_i = 1
        for i, c in enumerate(expression):
            if c=='{':
                brace_no += 1
            elif c == '}':
                brace_no -= 1
                if brace_no == 0:
                    end_idx = i
                    break
            elif c==',' and brace_no == 1:
                ret = ret.union(self.braceExpansionII(expression[last_i: i])) 
                last_i = i+1
        if last_i!=1: #for union
            ret = ret.union(self.braceExpansionII(expression[last_i:end_idx]))
        else:
            ret = self.braceExpansionII(expression[1:end_idx])
        if end_idx < len(expression)-1:
            ret = self.zip(list(ret), self.braceExpansionII(expression[end_idx+1:])) #WA 一次 一开始没有写self.zip导致调用系统默认的zip
            #用itertools.product 代替self.zip 56ms -> 48ms
            #ret = map(''.join, itertools.product(list(ret), self.braceExpansionII(expression[end_idx+1:])))
        ret = sorted(list(ret))
        if debug:
            print("For expression ", expression, "returning ",ret)
        return ret
           
sol = Solution()
ss = ["{{a,z},a{b,c},{ab,z}}", "{a,b}{c,{d,e}}", "ab{a,b,c}"]
for s in ss:
    print(sol.braceExpansionII(s))
