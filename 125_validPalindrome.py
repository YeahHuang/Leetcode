class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        for c in s:
            if c.isdigit() or c.islower() or c.isupper():
                if c.isupper():
                    ss += c.lower()
                else:
                    ss += c
        #以上可以用一句话完成 甚至么的额外空间 注意python str自带isalnum 的判断函数
        # s = ''.join(e for e in s if e.isalnum()).lower()
        
        return ss == ss[::-1]
    
        #sol2 是用双向指针， l,r 自己判断回文，也是很简单易懂的，这里不赘述了