class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        is_valid = True
        delete_flag = False
        while l<r:
            if s[l] != s[r]:
                is_valid =  (s[l+1]==s[r] and s[l+1:r+1] == s[l+1:r+1][::-1]) or (s[l]==s[r-1] and s[l:r]==s[l:r][::-1])
                break
                '''
                #WA 主要是if s[l+1] == s[r] or s[l] == s[r-1] 存在两个都相等的情况，其实是要搞清楚具体删哪一个的。 
                if delete_flag:
                    is_valid = False
                    break
                else:
                    if s[l+1] == s[r] or s[l] == s[r-1]:
                        delete_flag = True
                        if s[l+1] == s[r]:
                            l += 1
                        else:
                            r -= 1
                    else:
                        is_valid = False
                        break
                '''                
            l += 1
            r -= 1
        return is_valid