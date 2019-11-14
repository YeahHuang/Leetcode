class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        counter = collections.Counter(text)
        return min(counter['b'],counter['a'],counter['n'],counter['l']//2, counter['o']//2)