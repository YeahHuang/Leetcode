class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        def CalNum(tree, startIdx, n) -> int:
            i = startIdx
            choosed = []
            choosed.append(tree[i])
            totalNum = 0
            while tree[i]==tree[startIdx]:
                i = i+1 #一开始看错题了 以为能循环 写成了i = (i+1) % n 
                totalNum+=1
                if i==n:
                    break
            if i!=n:
                choosed.append(tree[i])
                while tree[i] in choosed:
                    i = i+1
                    totalNum+=1
                    if i==n:
                        break
            return totalNum

        n = len(tree)
        maxNum = 0  #一开始忘记先定义
        if n>0:
            maxNum = CalNum(tree,0,n)
        debug = False
        for i in range(1,n-1):
            if tree[i]!=tree[i-1]: #一开始连这个优化都没加 可惜了。 
                maxNum = max(maxNum, CalNum(tree, i, n))
                if debug:
                    print(maxNum)
        return maxNum

#下面是solution里的python2的做法 
class Solution:
    def totalFruit(self, tree):
        blocks =[(k, len(list(v))) for k, v in itertools.groupby(tree)]  #用这个来做元组很酷
        '''
('k:', 1) ('v:', [1])
('k:', 2) ('v:', [2, 2])
('k:', 1) ('v:', [1])
('k:', 2) ('v:', [2])
('k:', 3) ('v:', [3])
('k:', 1) ('v:', [1])
        '''
        debug = True
        if debug:
            print(blocks)
        #[1,2,2,1,2,3,1]
        #[(1, 1), (2, 2), (1, 1), (2, 1), (3, 1), (1, 1)]

        ans = i = 0
        if i< len(blocks):
            types, weight = set(), 0 
            for j in xrange(i, len(blocks)):
                types.add(blocks[j][0])
                weight += blocks[j][1]
                if len(types) >= 3:
                    i = j-1
                    break
                ans = max(ans, weight)
            else: #我真实的觉得这句话可能完全没有必要？？？ 见下方Ps
                break
        return ans
'''
这次才知道自己对xrange的了解还如此浅薄
>>> for i in xrange(5):
...   print(i)
... 
0
1
2
3
4
>>> for i in xrange(5):
...   print(i)
... else:
...   print(100)
... 
0
1
2
3
4
100
>>> for i in xrange(5):
...   print(i)
...   if i==3:
...     break
... else:
...   print(100)
0
1
2
3


'''
