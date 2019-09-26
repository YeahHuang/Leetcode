class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cur = triangle[0]
        for ll in triangle[1:]:
            cur.append(float('inf'))
            cur = [min(cur[i],cur[i-1])+num  for i, num in enumerate(ll)]
        return min(cur)
    