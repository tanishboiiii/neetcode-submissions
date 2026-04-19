class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in indices:
                return sorted([i, indices[compliment]])

            indices[nums[i]] = i
