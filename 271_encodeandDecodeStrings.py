#Sol1 unichr out of valid ascii
class Codec:
    def encode(self, strs):
        if len(strs) == 0:
            return unichr(258)
        return unichr(257).join(s for s in strs)
        #return unichr(257).join(s.encode('utf-8') for s in strs) 
        #原答案⬆️是加了这个encode('utf-8')的 但是我没加也还是过了 
    def decode(self, s):
        if s == unichr(258):
            return []
        return s.split(unichr(257))

#Sol2 @Stafan
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return ''.join("%d:"%(len(s)) + s for s in strs)
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        i = 0
        ret = []
        while i < len(s):
            j = s.find(':',i)
            i = j + int(s[i:j]) + 1 #一开始写成了 @int([i:j]) 忘记s[]了 还一直找不到哈哈
            ret.append(s[j+1:i])
        return ret

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

#Sol2.1 also length
class Codec:
    def len_to_str(self, x):
        """
        Encodes length of string to bytes string
        """
        x = len(x)
        bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)] #这个 (i*8) && 0xff 可以学习一下 但其实没啥必要
        bytes.reverse()
        bytes_str = ''.join(bytes)
        return bytes_str
    
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        # encode here is a workaround to fix BE CodecDriver error
        return ''.join(self.len_to_str(x) + x.encode('utf-8') for x in strs)
        
    def str_to_int(self, bytes_str):
        """
        Decodes bytes string to integer.
        """
        result = 0
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        return result
    
    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        i, n = 0, len(s)
        output = []
        while i < n:
            length = self.str_to_int(s[i: i + 4])
            i += 4
            output.append(s[i: i + length])
            i += length
        return output
