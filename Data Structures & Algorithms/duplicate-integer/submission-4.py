class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dupp = set(nums)
       
        if len(no_dupp) == len(nums):
            return False
        else:
            return True