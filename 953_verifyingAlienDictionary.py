class Solution:
    def isSmaller(self, s1, s2, hash_order):
        """
        #first few same and length dif
        """
        i = 0
        while i<len(s1) and i < len(s2):
            if hash_order[s1[i]] > hash_order[s2[i]]:
                return False
            elif hash_order[s1[i]] < hash_order[s2[i]]:
                return True
            i += 1
        #all same in the beginning
        if len(s1) < len(s2):
            return True
        else:
            return False
        
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #下面这3行可以用order_index = {c: i for i, c in enumerate(order)}来优雅的代替
        hash_order = {}
        for i, c in enumerate(order):
            hash_order[c] = i

        for i in range(len(words)-1):
            if self.isSmaller(words[i], words[i+1], hash_order) == False:
                return False
        return True 



    def isAlienSorted(self, words, order):
        m = {c: i for i, c in enumerate(order)}
        words = [[m[c] for c in w] for w in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))

        
    def isAlienSorted(self, words, order):
        return words == sorted(words, key=lambda w: map(order.index, w))