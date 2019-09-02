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
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        '''
        #一开始条件反射的写了⬇️ 不是很OK啊 没有读懂buf的定义
        while n>0:
            buf.append(read4(buf))
            n-=4
        '''
        idx = 0 
        while n>0:
            buf4 = [""] * 4
            count = read4(buf4)
            if count == 0:
                return idx #一开始只break 忘记return idx 了
            buf[idx: idx+min(count, n)] = buf4[:min(count, n)]
            idx += min(count, n)
            n-=4
        return idx