class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        #cells[0] = cells[-1] = 0 WA一次 自作聪明 其实会让最初的弄错
        er = [1<<i for i in range(8)]  #ps 这里用 er[] 和 直接 1<<j 无速度差别 但看着可能更清晰吧
        m = [-1] * (1<<8)
        state = 0 
        for i in range(8):
            if cells[i]:
                state += 1<<i
        m[state] = 0
        memo = []
        memo.append(state)
        for i in range(1,N+1): #ps 一开始这里写的是 for i in range(N) 然后⬇️再用i+1 怪别扭的 代码就要怎么清晰怎么来呀
            #print(bin(state)) bin()的用法还是google了的 要熟练呀
            new_state = state 
            for j in range(1, 7):
                if int((state & er[j-1])>0) ^ int((state & er[j+1])>0)==0:
                    new_state |= er[j]
                elif state & er[j]:
                    new_state -= er[j]
            state = new_state
            if state & 1:
                state -= 1
            if state & er[7]:
                state -= er[7]
            if m[state]!=-1:
                zhou_qi = i-m[state]
                state = memo[m[state]+(N - i) % zhou_qi]
                break
            else:
                m[state] = i
                memo.append(state)
        for i in range(8):
            cells[i] = 1 if (state & er[i]) else 0
        return cells
        
    #Intuition： 自己暴力枚举周期 遂去掉了seen 很奇妙 44ms 
    def prisonAfterNDays(self, cells, N):
        N -= max(N - 1, 0) // 14 * 14
        for i in range(N):
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
        return cells

    #56ms
    def prisonAfterNDays(self, cells, N):
        seen = {str(cells): N}
        while N:
            seen.setdefault(str(cells), N)
            N -= 1
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
            if str(cells) in seen:
                N %= seen[str(cells)] - N
        return cells



class Solution(object):
    def prisonAfterNDays(self, cells, N):
        def nextday(cells):
            return [int(i > 0 and i < 7 and cells[i-1] == cells[i+1]) #判断简明清晰
                    for i in xrange(8)]
        seen = {}
        while N > 0:
            c = tuple(cells) #它这个用tuple就清晰很多 
            if c in seen:
                N %= seen[c] - N
            seen[c] = N 

            if N >= 1:
                N -= 1
                cells = nextday(cells)
                
        return cells