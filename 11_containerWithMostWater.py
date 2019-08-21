class Solution:
    def maxArea(self, height: List[int]) -> int:
        #最远且大的肯定是max 近&大的差距 就在于 delta_height * smaller_width + dalta_width * smaller_height
        n = height
        if n<=2: return 0
        l, r = 0, n-1
        max_area = min(height[0],height[n-1])*(n-2)
        while l<r:
            if height[l]<height[r]:
                l += 1
            else:
                r -= 1 
            max_area = max(max_area, min(height[l],height[r])*(l-r-1))
        return max_area