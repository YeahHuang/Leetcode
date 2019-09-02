"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    def __init__(self):
        self.left = []
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        if self.left != []:
            if n>=len(self.left): #WA一次 一开始没考虑n>len(self.left)的情况
                buf[0:] = self.left[:]
                idx, n = len(self.left), n-len(self.left)
                self.left=[]
            else:
                buf[0:] = self.left[:n]
                idx, self.left, n = n, self.left[n:], 0 #一开始没有考虑n的置0 WA一次
        else:
            idx = 0
        while n>0:
            buf4 = [""] * 4
            count = read4(buf4)
            if count == 0:
                return idx 
            if count>n:
                buf[idx: idx+n] = buf4[:n]
                self.left = buf4[n:]
                idx += n
                n -= 4
            else:
                buf[idx: idx+count] = buf4[:count]
                idx += count
                n-=4
        return idx