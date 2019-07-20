#7.20 19:58-21:22 84min 3sol

class Codec:
 
    alphabet = string.ascii_letters + string.digits #拼写啥的可以记一记

    #Sol 1 保密性高 查询时间长 
    #Refefenced from https://leetcode.com/problems/encode-and-decode-tinyurl/discuss/100341/Easy-to-Understand-in-Python
    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.url2code:#一开始写成了self.url2code.keys() 其实不用这么麻烦滴
            while True:
                code = ''.join(random.choice(Codec.alphabet) for _ in range(6)) 
                #一开始直接写了alphabet 这里需要学习下class里变量的引用
                #for _ 这样的写法 和 for i 一样很可爱对吧
                #random.choice 用法 + ''.join 而不是返回list的做法也不错哦
                if code not in self.code2url.keys():
                    self.url2code[longUrl] = code
                    self.code2url[code] = longUrl
                    break
            return 'http://tinyurl.com/'+self.url2code[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.code2url[shortUrl.split('/')[-1]]

    #Sol2.0 查询快 但很容易被黑
    def __init__(self):
        self.urls = []

    def encode(self, longUrl):
        self.urls.append(longUrl)
        return 'http://tinyurl.com/'+str(len(self.urls)-1)

    def decode(self, shortUrl):
        return self.urls[int(shortUrl.split('/')[-1])]  

     #Sol2.1 相当于把普通的int转化成62进制的数 
     def encode(self, longUrl):
        self.urls.append(longUrl)
        qpp = len(self.urls) - 1 
        code = ""
        while qpp > 0: 
            code += Codec.alphabet[qpp%62] 
            qpp //= 62
        return 'http://tinyurl.com/'+code

    def decode(self, shortUrl):
        code = shortUrl.split('/')[-1]
        qpp = 0
        for c in code:
            if c.isdigit():
                qpp = qpp * 62 + (c-'0') + 52 #alphabet[52] = '0'
            elif c<='z':
                qpp = qpp * 62 + (c-'a') + 0  #alphabet[0] = 'a'
            else:
                qpp = qpp * 62 + (c-'A') + 26 #alphabet[26] = 'A'
        return self.urls[qpp]


