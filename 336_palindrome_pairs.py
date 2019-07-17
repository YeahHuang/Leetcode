class Solution:

    #Sol1 O(n*n*w) TLE
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        palindrom_pairs = []
        for i in range(n):
            for j in range(i+1, n):
                s = words[i] + words[j]
                if s[::-1] == s:
                    palindrom_pairs.append([i,j]) #一开始写成+= 会自动连接成一维list 而不是独立的pairs
                s = words[j] + words[i]
                    palindrom_pairs.append([j,i])
        return palindrom_pairs
    #Sol2 O(n*w*w) 360ms 看起来很短 但是对于["abcd","dcba"] & ["bob",""] 这样的判断WA一次
    #改编自 https://leetcode.com/problems/palindrome-pairs/discuss/79209/Accepted-Python-Solution-With-Explanation
    def palindromePairs(self, words):
        m_words = {word:i for i,word in enumerate(words)}
        m_reversed_words = {word[::-1]:i for i, word in enumerate(words)}
        for i, word in enumerate(words):
            for j in range(len(word)):
                pref = word[:j]
                suff = word[j:]
                if pref[::-1]==pref and suff in m_reversed_words and m_reversed_words[suff]!=i:
                    palindrom_pairs.append([m_reversed_words[suff],i])
                if suff[::-1]==suff and pref in m_reversed_words and m_reversed_words[pref]!=i:
                    palindrom_pairs.append([i, m_reversed_words[pref]])
                    if j==0: #pref == "" 这里不能忘吖！
                        palindrom_pairs.append([m_reversed_words[""],i])
    #Sol3 TRIE
    #https://leetcode.com/problems/palindrome-pairs/discuss/79195/O(n-*-k2)-java-solution-with-Trie-structure
    #https://www.cnblogs.com/dolphin0520/archive/2011/10/11/2207886.html
        #自己写的 sort+查找 WA 因为比较的left right的界限很难判定的
        def isPalindrom(s1:str, s2:str) -> bool:
            if len(s1)>len(s2):
                s1,s2 = s2, s1
            return s2[:len(s1)] == s1 and s2[len(s1):][::-1] == s2[len(s1):]
        
        new_words = [(word, i) for i,word in enumerate(words)]
        reversed_words = [(word[::-1],i, len(word)) for i,word in enumerate(words)] #那个xxx字典树 判断前缀后缀贼有用那个
        new_words.sort()#可以先不考虑 直接排
        #后续优化： 加一个.pop怎么样呀 
        reversed_words.sort()
        debug = False
        if debug: 
            print(reversed_words)
            print(isPalindrom("ssss",""), isPalindrom("","sss"), isPalindrom("ls","lssss"))
        reversed_word, idx, length_r = reversed_words[0]
        if length_r == 0:
            for i, word in enumerate(words):
                if i!=idx and word[::-1]==word:
                    palindrom_pairs.append([i,idx])
            reversed_words.pop(0)
        n = len(reversed_words)
        for i, word in enumerate(words): #短&> break 长&< break 
            l = 0
            r = n-1
            length = len(word)
            while l<r:
                m = (l+r)//2
                if debug:
                    print(i,l,r,m,reversed_words[m])
                reversed_word, idx, length_r = reversed_words[m]
                break_flag = True
                if length_r < length and reversed_word > word:
                    r = m - 1
                    break_flag = False
                if length_r > length and reversed_word < word:
                    l = m + 1 
                if break_flag:
                    break
            for j in range(l, r+1):
                reversed_word, idx, length_r = reversed_words[j]
                if idx!=i and isPalindrom(word, reversed_word):
                    palindrom_pairs.append([i, idx])
                                            