class Solution:
    def decodeString(self, s: str) -> str:
        
        #Sol1: dfs 32ms
        def dfsDecode(s:str):
            decode_s, i, n, debug = "", 0, len(s), False
            if debug:
                print(s)
            while i<n:
                if s[i].isdigit():
                    start_idx = i
                    while i<n and s[i].isdigit():
                        i += 1
                    k = int(s[start_idx:i])
                    if s[i]!='[':
                        print("ERROR! not [] after num i=%d"%(i))
                        break
                    paren_num = 0
                    start_idx = i + 1
                    while i<n:
                        if s[i]=='[':   paren_num += 1
                        if s[i]==']': 
                            paren_num -= 1
                            if paren_num == 0:
                                if debug:
                                    print("Is going to calculate from %d to %d"%(start_idx, i))
                                decode_s +=  k * dfsDecode(s[start_idx:i])
                                #一开始这里写了 i+1导致 错误
                                break
                        i += 1
                elif s[i].isalpha():
                    decode_s += s[i]
                i += 1
            return decode_s
        return dfsDecode(s)

        #Sol2 36ms
        def stackDecode(s:str):
            decode_s, i, n, debug = "", 0, len(s), True
            nums = []
            strs = [""]
            while i < n:
                if s[i].isdigit():
                    start_idx = i
                    while i<n and s[i].isdigit():
                        i += 1
                    k = int(s[start_idx:i])
                    nums.append(k)
                elif s[i].isalpha():
                    start_idx = i
                    while i<n and s[i].alpha():
                        i += 1
                    strs.append(s[start_idx:i])
                elif s[i] == '[':
                    i += 1
                elif s[i] == ']':
                    k, s0 = nums.pop(), strs.pop()
                    if debug:
                        print("k = %d s0=%s"%(k, s0a))
                    strs.append(k*s0)
                    i += 1



                                
