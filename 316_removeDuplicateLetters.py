class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        #突破点1(已想到): 贪心 若当前最小的元素 有duplicate 则必然选择最left的 
        #突破点2: 
        '''
        我自己思考的时候的内心os： 
        #为什么我会觉得只要直接贪心？ a肯定留下最前的 b在a后面 但尽量前的？ 有一些必须要留着的字母是不是很麻烦 
        #有一些字符可以挡在另外的数字前面 就很爽
        #a 和 z很好确定 问题就是比如从b开始 如果前面有z 那选最小的， 但有a 它就需要是在a后面的最前的位置了
        
        注意ans只有26位 按照这一位是原来的什么 也OK？
        因为min & max 是必须确定的所以只有24 

        #a z b只有2个选择 最前 or 最前 after a
        #y 也只有2个 最后 or last before z  其实只要有任何后面的最前 > now 必然尽量往前 
        #greedy 把前半段的尽量往前 后半段的就尽量往后？  
        '''

        #其实很接近了 只要后面还有就都先移除 直到找到一个最佳的此时最小的pos
        if not s: 
            return ""
        cnt = collections.Counter(list(s))
        pos = 0
        for i, c in enumerate(s):
            if c < s[pos]: 
                pos = i
            cnt[c] -= 1
            if cnt[c] == 0:
                break
        return s[pos] + self.removeDuplicateLetters(s[pos+1:].replace(s[pos],""))


'''collections容器： Counter是对于python dict的一个封装
Link: https://docs.python.org/zh-cn/3/library/collections.html
要学的要补充的还有好多呀
>>> c = Counter()                           # a new, empty counter
>>> c = Counter('gallahad')                 # a new counter from an iterable
>>> c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
>>> c = Counter(cats=4, dogs=8)  

>>> # 用它来找高频词
>>> import re
>>> words = re.findall(r'\w+', open('hamlet.txt').read().lower())
>>> Counter(words).most_common(10)
[('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
 ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]
'''