from operator import itemgetter, attrgetter
import collections, heapq, functools

class Solution:
    #Sol1 NlgN
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''
        Python-sort 官方link： https://docs.python.org/3.3/howto/sorting.html 
        一开始写了这个compare 但是读官方文档才知道在python3.x中cmp这个参数已经被删除了
        def compare(x,y): 
            if x[1] > y[1] or (x[1]==y[1] and x[0]>y[0]):
                cmp = 1
            elif (x[1]==y[1] and x[0]==y[0]):
                cmp = 0
            else:
                cmp = -1
            return cmp
        '''
        cnt = list(collections.Counter(words).items())
        cnt = [(s,-times) for s,times in cnt]
        cnt.sort(key=itemgetter(1,0))
        return [s for s, times in cnt[:k]]
        '''
        p.s. 我一开始在这里捣鼓了很久 因为想要写出像 #347 zip中return list(zip(*collections.Counter(nums).most_common(k)))[0] 
        的酷酷的表达。 但一直失败 google后搜索到了是这样的：
        python2只需要 list(zip(*cnt)[0])
        但python3 要 list(list(zip(*cnt))[0])
        我当时少了一个list 以后可以记住一下啦～
        '''

        #Sol 另一种 所以其实python的自带sort 就会2个依次比较的吖
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = collections.Counter(words)
        candidates = cnt.keys()
        cnt.sort(key = lambda w: (-cnt[w],w))
        return candidates[:k]

         #Sol2 N + KlgN 用堆来pop前K个 76ms -> 64ms

from heapq import heapify, heappush, heappop
class WordFreq:
    def __init__(self, word, times):
        self.word = word
        self.times = times

    def __lt__(self, other):
        if self.times != other.times:
            #return self.times.__lt__(other.times)
            return self.times < other.times #直接法更快 72ms > 64ms
        else:
            #return self.word.__gt__(other.word)
            return self.word > other.word

    '''
    #根据验证此段可有可无 但是也不知道为什么 有了反而快 76ms -> 68ms
    def __eq__(self, other):
        return self.count == other.count and self.word == other.word
    '''

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = collections.Counter(words).items()
        k_most_frequent = []
        heapq.heapify(k_most_frequent)
        debug = False
        for word, times in cnt:
            if debug:  print(word,times)
            heappush(k_most_frequent,  WordFreq(word, times))
            if len(k_most_frequent) == k+1:
                heappop(k_most_frequent)
        return reversed([heappop(k_most_frequent).word for i in range(k)])


#Sol 2.1 唯一的区别在于用了functools 但实际更慢一些 https://leetcode.com/problems/top-k-frequent-words/discuss/190691/Python-O(nlogk)-Time-O(n)-Space
@functools.total_ordering #待学习 functools: https://docs.python.org/2/library/functools.html
class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word
        
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
    
    

