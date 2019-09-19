class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l, r = max(sum(weights)//D, max(weights)), sum(weights) #WA 一次 一开始写成了min(weights)
        while l < r:
            mid, cur, need = (l+r)//2, 0, 1
            for w in weights:
                if cur+w<=mid:
                    cur += w
                else:
                    cur = w
                    need += 1
            if need > D:
                l = mid + 1
            else:
                r = mid
        return r