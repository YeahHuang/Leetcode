# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """
#Sol1 my 
class Solution:
    def findSecretWord(self, wordList, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def calMatch(w1, w2):
            cnt = 0
            for i in range(6):
                if w1[i]==w2[i]:
                    cnt += 1
            return cnt
        
        t = [[set() for _ in range(6)] for i in range(len(wordList))]
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                qpp = calMatch(wordList[i],wordList[j])
                t[i][qpp].add(j)
                t[j][qpp].add(i)
                
        cur = set([i for i in range(len(wordList))])
        it = 0
        while it < 10:
            i = random.choice(list(cur)) #WA1 这里直接 cur.pop(0)
            cur.remove(i)   #WA2 random后自己又忘记remove了
            qpp = master.guess(wordList[i])
            if qpp == 6:
                break
            cur &= t[i][qpp]
            it += 1

#Sol 1.1 一点点minmax的思想 @lee215 (25/26)**6 ~ 80%的概率是0的 我们要把关系为0最多的那个挑出来 这样就能排除最多         
class Solution:
    def findSecretWord(self, wordlist, master):
        def calMatch(w1, w2):
            cnt = 0
            for i in range(6):
                if w1[i]==w2[i]:
                    cnt += 1
            return cnt
        n = 0
        while n < 6:
            count = collections.Counter(w1 for w1, w2 in itertools.permutations(wordlist, 2) if calMatch(w1, w2) == 0)
            guess = min(wordlist, key=lambda w: count[w])
            n = master.guess(guess)
            wordlist = [w for w in wordlist if calMatch(w, guess) == n]


#Sol 2 更加现实 就是要把和别的相关度最大的单词挑出来 这样排出可排出更多
class Solution(object):

    def findSecretWord(self, wordlist, master):
        
        def pair_matches(a, b):         # count the number of matching characters
            return sum(c1 == c2 for c1, c2 in zip(a, b))

        def most_overlap_word():
            counts = [[0 for _ in range(26)] for _ in range(6)]     # counts[i][j] is nb of words with char j at index i
            for word in candidates:
                for i, c in enumerate(word):
                    counts[i][ord(c) - ord("a")] += 1

            best_score = 0
            for word in candidates:
                score = 0
                for i, c in enumerate(word):
                    score += counts[i][ord(c) - ord("a")]           # all words with same chars in same positions
                if score > best_score:
                    best_score = score
                    best_word = word

            return best_word

        candidates = wordlist[:]        # all remaining candidates, initially all words
        while candidates:

            s = most_overlap_word()     # guess the word that overlaps with most others
            matches = master.guess(s)

            if matches == 6:
                return

            candidates = [w for w in candidates if pair_matches(s, w) == matches]  