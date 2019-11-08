class Solution:
    def confusingNumber(self, N: int) -> bool:
        s = list(str(N))
        if '2' in s or '3' in s or '4' in s or '5' in s or '7' in s:
            return False
        if len(s)&1 and s[len(s)//2] in {'6','9'}:
            return True
        equals_reverse = True
        for i in range(len(s)//2):
            if (s[i] == '6' and s[-i-1] != '9') \
            or (s[i] == '9' and s[-i-1] != '6') \
            or (s[i] in {0,1,8} and s[i] != s[-i-1]):
                equals_reverse = False
                break
        return equals_reverse == False