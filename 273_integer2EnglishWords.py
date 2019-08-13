#p.s. 此题最大的体会是不要被hard直接吓坏了！ 或者至少自己先失一个吖 不要闷着头
#多写了很多And 用了些tricks 以后吸取教训吧
class Solution:
    def numberToWords(self, num: int) -> str:
        #1024 1 100 1000 1010000  1,000,100,010, 1 1,234,056,789
        #用' '.join来写是不是要酷很多 
        #可能需要一个and flag 或者把相邻的and删除 
        def hundredToWords(s:str) -> list:
            qpp = []
            i = 2
            if debug:
                print(s)
                print(s[0],s[1],s[2])
            if s[i-2]>'0':
                qpp = qpp + [digits[int(s[i-2])]] + ['Hundred']
            elif s[i-1]>'0' or s[i]>'0':
                qpp += ['And']
            if s[i-1]>'0':
                if s[i]=='0':
                    qpp += [tens[int(s[i-1])]]
                elif s[i-1]=='1':
                    qpp += [digits[int(s[i-1:i+1])]]
                else:
                    qpp +=  [tens[int(s[i-1])]] + [digits[int(s[i])]]
            elif s[i]>'0': #ten = 0 
                if s[i-2]>'0':
                    qpp += ['And']
                qpp += [digits[int(s[i])]]

            return qpp 

        s = str(num)
        i = len(s) - 1
        words = []
        digits = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen', 'Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        tens = ['Zero','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        bigs = ['','Thousand','Million','Billion']
        bigs_idx = 0 
        debug = False
        while i>=2:
            if s[i-2:i+1] == '000':
                words = ['And'] + words #一开始写成了words.append('And')
                i -= 3
                bigs_idx += 1
                continue
            words = hundredToWords(s[i-2:i+1]) + [bigs[bigs_idx]] + words
            if debug:
                print(i, hundredToWords(s[i-2:i+1]), [bigs[bigs_idx]], words )
            bigs_idx += 1
            i -= 3
        if i>=0:
            qpp = hundredToWords((2-i)*'0'+s[:i+1])
            words = qpp + [bigs[bigs_idx]] + words
        words.pop() #pop掉最后一个 ''
        if len(words)>0 and words[0] == 'And':
            words.pop(0)
        i, end_idx = 0, len(words) 
        while i < end_idx - 1:
            if words[i]=='And' and words[i+1]=='And':
                words.pop(i)
                end_idx -= 1
            else:
                i += 1
        i, end_idx = 0, len(words) 
        while i < end_idx - 1:
            if words[i]=='And':
                words.pop(i)
                end_idx -= 1
            else:
                i += 1

        return " ".join(words) if len(words)>0 else "Zero"

#Referenced from @Stafan More concise
def numberToWords(self, num):
    to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split() #很聪明的写法
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    def words(n):
        if n < 20:
            return to19[n-1:n]
        if n < 100:
            return [tens[n/10-2]] + words(n%10)
        if n < 1000:
            return [to19[n/100-1]] + ['Hundred'] + words(n%100)
        for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
            if n < 1000**(p+1):
                return words(n/1000**p) + [w] + words(n%1000**p)
    return ' '.join(words(num)) or 'Zero'


sol = Solution()
test_cases = [1024,1,100,1000,1010000, 1000100010, 1234056789, 12,10,0,100000001]
for num in test_cases:
    print(num,": ",sol.numberToWords(num))