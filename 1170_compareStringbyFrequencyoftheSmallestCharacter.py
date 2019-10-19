from string import ascii_lowercase
from bisect import bisect_right
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        #freq = sorted([self.calFrequency(word) for word in words])
        freq = sorted(w.count(min(w)) for w in words)
        return [len(freq)-bisect_right(freq, self.calFrequency(word)) for word in queries]
    
    def calFrequency(self, word):
        counter = collections.Counter(word)
        for c in ascii_lowercase:
            if c in counter:
                return counter[c]
        return 0