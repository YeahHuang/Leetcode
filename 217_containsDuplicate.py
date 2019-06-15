class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
        #如果是c++ int[] nums.     return (new HashSet<int>(nums)).Count != nums.Length; 