# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        l = 0           #l-false  r-true
        r = n + 1
        while l < r-1:
            m = (l+r)//2
            if isBadVersion(m):
                r = m
            else:
                l = m
        return r