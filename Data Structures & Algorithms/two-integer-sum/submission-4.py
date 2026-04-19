class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index in range(len(nums)):
            # if nums[index] is the right answer, then 
            # we must have target - nums[index] later in
            # the array...      

            curr_element = nums[index] 
            if curr_element in seen:
                ans = [index, seen[curr_element]]
                return sorted(ans)


            potential_candidate = target - nums[index]
            seen[potential_candidate] = index

        ret