class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l,r = 0, n-1
        ans = [-1, -1]
        while l<r:
            mid = (l+r)//2
            if nums[mid]==target:
                start_idx = mid
                while start_idx>=1 and nums[start_idx-1]==target:   #如果用二分来完成这个部分会更快
                    start_idx -= 1
                end_idx = mid
                while end_idx+1<n and nums[end_idx+1]==target:
                    end_idx += 1
                ans =[start_idx, end_idx]
                break
            elif nums[mid]<target:
                l = mid + 1
            else:
                r = mid - 1
        if ans == [-1,-1] and l==r and ans[l] == target:
            ans = [l, l]
        return ans

    def extreame_insertion_index(self, nums, target):#其实别人25ms 我跑出来都是100ms 仅供参考 
        n = len(nums)
        l,r = 0, n-1
        ans = [-1, -1]

        while l<=r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        ans[0] = l

        l, r = 0, n-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        ans[1] = r
        if ans[0]>ans[1]:
            ans = [-1,-1]
        return ans
