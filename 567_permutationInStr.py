class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = collections.Counter(s1)
        set1 = set(counter1.keys())
        dict2 = collections.defaultdict()
        len1, hit2, start = len(s1), 0, -1
        for i, c in enumerate(s2):
            if c not in set1:
                if start != -1:
                    start = -1 
            elif start!=-1:
                if dict2.get(c,0)<counter1[c]:
                    dict2[c] = dict2.get(c,0) + 1
                    hit2 += 1
                    if hit2==len1:
                        break
                else:
                    '''
                    WA一次 dcda cda 其实最开始考虑到这种情况的 但写着写着就忘了。 感觉面试的时候草稿还是要清晰一点 不然边写边忘
                    dict2 = collections.defaultdict()
                    dict2[c] = 1
                    hit2 = 1
                    '''
                    while s2[start]!=s2[i]:
                        hit2 -= 1
                        dict2[s2[start]] -= 1
                        start += 1
                    if start != i:
                        start += 1
            else:
                start = i
                dict2 = collections.defaultdict()
                dict2[c] = 1
                hit2 = 1
                
        return hit2==len1