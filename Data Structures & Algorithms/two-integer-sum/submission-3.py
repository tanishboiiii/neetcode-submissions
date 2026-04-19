class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            possible = target - nums[i]
            if possible in seen:
                return [seen[possible], i]
            
            seen[nums[i]] = i


        
