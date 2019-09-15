#Referenced from @Strefan
class Solution:
    #简洁版 next iter的使用
    def numMatchingSubseq(self, S, words):
        waiting = collections.defaultdict(list)
        for it in map(iter, words):
            waiting[next(it)].append(it)
        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])

    #容易理解版
    def numMatchingSubseq(self, S, words):
        ans = 0
        waiting = collections.defaultdict(list) #当然也可以是[[] for _ in range(26)]但是不用python自带的dict感觉亏一些
        for word in words:
            it = iter(word)
            waiting[next(it)].append(it)
        print(waiting)
        for c in S:
            old_bucket = waiting[c]
            waiting[c] = []
            while old_bucket:
                it = old_bucket.pop()
                nxt = next(it, None)
                if nxt:
                    waiting[nxt].append(it)
                else:
                    ans += 1
        return ans