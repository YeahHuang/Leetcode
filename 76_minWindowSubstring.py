class Solution:
    #112ms beats80%
    def minWindow(self, s: str, t: str) -> str:
        dict_t = collections.Counter(t)
        set_t = set(dict_t.keys())
        start = 0
        summ = collections.defaultdict()
        len_summ, len_t, min_w, min_window = 0, len(t), len(s)+1,""
        #把len_summ len_t 改为hit_summ, needed 可能更好理解一些
        for i in range(len(s)):
            if s[i] in set_t:
                summ[s[i]] = summ.get(s[i],0) + 1
                if summ[s[i]] <= dict_t[s[i]]:
                    len_summ += 1
                    if len_summ == len_t:
                        while (s[start] not in set_t) or (summ[s[start]] > dict_t[s[start]]):
                            if s[start] in set_t:
                                summ[s[start]] -= 1
                            start += 1
                        if min_w > i - start + 1:
                            min_w = i - start + 1
                            min_window = s[start:i+1]
                        if s[start] in set_t:
                            summ[s[start]] -= 1
                            len_summ -= 1 #WA一次 一开始这里忘记写了 多变量要注意变化呀 
                        start += 1
        return min_window