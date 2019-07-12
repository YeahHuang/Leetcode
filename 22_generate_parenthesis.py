class Solution:
    def generateParenthesis(self, n: int) -> List[str]: #28ms
        #bfs 一层一层的套 balance
        if n==0:
            return []
        cur_paren  = ['(']
        cur_balance = [1]
        debug = False
        for step in range(2,n*2):
            next_paren = []
            next_balance = []
            if debug:
                print(cur_paren)
                print(cur_balance)
            for i in range(len(cur_paren)):
                if cur_balance[i]>0:
                    next_paren.append(cur_paren[i] + ')')
                    next_balance.append(cur_balance[i] - 1)
                if n*2 - step > cur_balance[i]:
                    next_paren.append(cur_paren[i] + '(')
                    next_balance.append(cur_balance[i] + 1)
            cur_balance = next_balance
            cur_paren = next_paren


        cur_paren = [s+')' for s in cur_paren]
        return cur_paren

        def generate(p, left, right, parens = []): #36ms 有评论说可能会include previous call 
            if left:        generate(p+'(', left-1, right)
            if right>left:  generate(p+')', left, right-1)
            if not right:   parens += p,
            return parens
        return generate('',n,n)

        def generate(p, left, right): #44ms
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p+'(', left-1, right):    yield q 
                #在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
                for q in generate(p+')',left, right-1):     yield q
        return list((generate('',n,n)))